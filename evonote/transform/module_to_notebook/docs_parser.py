from __future__ import annotations

import inspect
import re
from typing import Dict, List, Tuple, Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from evonote.transform.module_to_notebook import module_struct

"""
This file is for parsing the docstring and comments in the module.
"""

"""
## Extract functions, classes and comments
"""


def get_in_module_structs(module, functions, classes, line_offset=0) -> List[
    module_struct]:
    # check whether the module has no source code
    try:
        module_src = inspect.getsource(module)
    except OSError:
        module_src = ""

    raw_comment_struct_list = prepare_raw_comment_struct(module_src)

    func_cls_structs = prepare_func_cls_struct(functions, classes, module_src,
                                               line_offset)

    structs = mix_cmt_cls_func_structs(raw_comment_struct_list, func_cls_structs)

    process_raw_comments(structs)

    return structs


def process_raw_comments(structs):
    for i, struct in enumerate(structs):
        if struct[0] == "raw_comment":
            comment_content = struct[1]
            comment_tokens = process_raw_comment_content(comment_content)
            structs[i] = ("comment", comment_tokens, struct[2])


"""
### Mix comments, functions and classes extracted

The mix is non-trivial because we discard the comments inside functions and classes
"""


def mix_cmt_cls_func_structs(cmt_structs, cls_func_structs) -> List[module_struct]:
    """
    Mix the comment_structs and cls_func_structs into a list of struct
    Discard the comments inside functions and classes
    :param cmt_structs: The comment_structs
    :param cls_func_structs: The cls_func_structs
    :return: A list of struct sorted by the start line
    """
    structs = []
    cmt_index = 0
    cls_func_index = 0
    while cmt_index < len(cmt_structs) and cls_func_index < len(cls_func_structs):
        cmt_struct = cmt_structs[cmt_index]
        cls_func_struct = cls_func_structs[cls_func_index]

        if cmt_struct[2][1] < cls_func_struct[2][0]:
            structs.append(cmt_struct)
            cmt_index += 1
        else:
            structs.append(cls_func_struct)
            curr_cls_func_end = cls_func_struct[2][1]
            cls_func_index += 1
            # discard the comments inside functions and classes
            i_delete = 0
            while i_delete < len(cmt_structs):
                cmt_end = cmt_structs[i_delete][2][1]
                if cmt_end < curr_cls_func_end:
                    i_delete += 1
                else:
                    break
            cmt_index = i_delete
    # # append the remaining structs
    # append the remaining comment_structs
    if (len(structs) > 0 and cmt_index < len(cmt_structs)
            and cmt_structs[-1][2][0] > cls_func_structs[-1][2][1]):
        structs.extend(cmt_structs[cmt_index:])

    if cls_func_index < len(cls_func_structs):
        structs.extend(cls_func_structs[cls_func_index:])


    if len(cls_func_structs) == 0:
        structs.extend(cmt_structs[cmt_index:])

    return structs


"""
### Extract functions and classes
"""


def add_func_cls_to_struct_list(struct_list: List[module_struct], func_cls_list,
                                line_start_pos, struct_type, line_offset):
    for func_cls in func_cls_list:
        struct_src, struct_start_line = inspect.getsourcelines(func_cls)
        struct_start_line = struct_start_line - line_offset - 1
        struct_end_line = struct_start_line + len(struct_src)
        start_pos = line_start_pos[struct_start_line]
        end_pos = line_start_pos[struct_end_line]
        struct_list.append((struct_type, func_cls, (start_pos, end_pos)))


def prepare_func_cls_struct(functions, classes, module_src, line_offset) -> List[
    module_struct]:
    """
    Transform the functions and classes into a list of module_struct
    :param functions: The functions in the module
    :param classes: The classes in the module
    :return: A list of module_struct sorted by the start line
    """
    src_lines = module_src.split("\n")
    line_start_pos = [0]
    for i in range(1, len(src_lines)):
        line_start_pos.append(line_start_pos[-1] + len(src_lines[i - 1]) + 1)

    structs = []
    add_func_cls_to_struct_list(structs, functions, line_start_pos, "function",
                                line_offset)
    add_func_cls_to_struct_list(structs, classes, line_start_pos, "class", line_offset)
    structs.sort(key=lambda x: x[2][0])
    return structs


"""
### Extract comments
"""
# three_quote_pattern is multi-line comment pattern

three_quote_pattern = re.compile(r'(^|\n)\s*?"""([^(""")]*?)"""', re.DOTALL)


def prepare_raw_comment_struct(parent_src: str) -> List[module_struct]:
    comment_struct_list = []
    matches = three_quote_pattern.finditer(parent_src)
    for match in matches:
        comment_content = match.group(2)
        comment_pos = match.span()
        comment_struct_list.append(("raw_comment", comment_content, comment_pos))
    return comment_struct_list


section_pattern = re.compile(r"(\n\s*?#+ .*)")


def process_raw_comment_content(comment_content):
    comment_tokens = []
    # Find all sections which should start with one or more # followed by a space
    section_matches = section_pattern.finditer(comment_content)
    last_section_end = 0
    for section_match in section_matches:
        section_markdown = section_match.group(1)[1:].lstrip()
        # find first non-# character
        section_title = section_markdown.lstrip("#")
        section_level = len(section_markdown) - len(section_title)
        section_title = section_title.strip()
        section_start, section_end = section_match.span()
        last_section_end = section_end
        comment_text_before_section = comment_content[:section_start]
        if len(comment_text_before_section) > 0:
            comment_tokens.append(
                ("text", comment_text_before_section, (0, section_start)))
        comment_tokens.append(
            ("section", (section_title, section_level), (section_start, section_end)))
    if last_section_end < len(comment_content):
        remaining_text = comment_content[last_section_end:].strip()
        if len(remaining_text) > 0:
            comment_tokens.append(("text", remaining_text,
                                   (last_section_end, len(comment_content))))
    return comment_tokens


"""
## Docstring parsers

The class and functions for parse the docstring of functions
"""

Doc_parser_res = Tuple[str, Dict[str, str], str]
Doc_parser = Callable[[str], Doc_parser_res]


class FunctionDocs:
    def __init__(self, general: str, params: Dict[str, str], returns: str):
        self.general: str = general if general is not None else ""
        self.params: Dict[str, str] = params if params is not None else {}
        self.returns: str = returns if returns is not None else ""


def parse_reStructuredText_docstring(raw_docs: str) -> Doc_parser_res:
    """
    Parse the docstring generated by PyCharm
    :param raw_docs: raw docstring
    :return: general, params, returns, keywords
    """
    state = "general"

    general = ""
    params = {}
    param_name = ""
    returns = ""
    doc_lines = raw_docs.split("\n")
    for line in doc_lines:
        content_start = 0
        if line.startswith(":param"):
            # find next :
            next_colon = line.find(":", 6)
            if next_colon != -1:
                param_name = line[6:next_colon].strip()
                state = "param"
                content_start = next_colon + 1
        elif line.startswith(":return:"):
            state = "return"
            content_start = 8

        content = line[content_start:]
        if state == "param":
            params[param_name] = params.get(param_name, "") + content.strip()
        elif state == "return":
            returns += content.strip()
        else:
            general += content.strip()
    return general, params, returns


def parse_google_docstring(raw_docs: str):
    """
    Parse the docstring generated by VSCode
    :param raw_docs:
    :return:
    """
    state = "general"
    general = ""
    params = {}
    param_name = ""
    returns = ""
    doc_lines = raw_docs.split("\n")
    for line in doc_lines:
        content_start = 0
        if line.startswith("Args:"):
            state = "param"
            content_start = 5
            continue
        elif line.startswith("Returns:"):
            state = "return"
            content_start = 8

        content = line[content_start:]
        if state == "param":
            # find next :
            next_colon = line.find(":")
            new_content = line
            if next_colon != -1:
                param_name = line[:next_colon].strip()
                state = "param"
                content_start = next_colon + 1
                new_content = line[content_start:]
            params[param_name] = params.get(param_name, "") + " " + new_content.strip()
        elif state == "return":
            returns += content.strip()
        else:
            general += content.strip()
    return general, params, returns
