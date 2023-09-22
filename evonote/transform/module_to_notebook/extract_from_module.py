from __future__ import annotations

import importlib
import inspect
import os
import pkgutil
from typing import Dict, List

from evonote.notebook.note import Note
from evonote.notebook.notebook import make_notebook_root
from evonote.transform.module_to_notebook import module_struct
from evonote.transform.module_to_notebook.docs_parser import parse_reStructuredText_docs, \
    parse_google_docs, FunctionDocs, Doc_parser, get_in_module_structs

"""
This modules is for extract the information from python modules and build a notebook for it.


## Get notebook for module

"""


def get_notebook_for_module(module, docs_parser_type="reStruct"):
    if docs_parser_type == "reStruct":
        docs_parser = parse_reStructuredText_docs
    elif docs_parser_type == "google":
        docs_parser = parse_google_docs
    else:
        raise ValueError("docs_parser_type should be pycharm or vscode")
    root_module = module
    root_path = module.__file__.split("__init__.py")[0]
    root_module_name = module.__name__
    note_root, notebook = make_notebook_root(
        "Notebook of module: " + root_module_name)
    tree = {"type": "module", "obj": root_module, "children": {},
            "name": root_module_name}
    get_module_members(root_module, tree, root_path)
    build_notebook_for_module(tree, note_root, docs_parser)
    return notebook


"""
## Put module members into tree
"""


def get_module_members(module, tree_root_node, root_path: str):
    classes, functions, sub_modules = find_sub_module_func_cls(module, root_path)

    add_structs_to_tree(classes, functions, module, tree_root_node)

    process_sub_modules(sub_modules, tree_root_node)

    return


def find_sub_module_func_cls(module, root_path):
    module_dir = os.path.dirname(inspect.getfile(module))
    sub_modules = []
    is_pkg = hasattr(module, "__path__")
    if is_pkg:
        for sub_module_info in pkgutil.iter_modules([module_dir]):
            sub_module = importlib.import_module(
                module.__name__ + "." + sub_module_info.name)
            sub_modules.append(sub_module)
    functions = []
    classes = []
    for name in dir(module):
        member = module.__dict__[name]
        # check the type of the member is in module, class, method, function
        if (str(type(member)) not in ["<class 'type'>",
                                      "<class 'function'>"]):
            continue
        # skip the members defined outside the root path
        try:
            member_path = inspect.getfile(member)
        except:
            continue
        if not member_path.startswith(root_path):
            continue

        if inspect.isclass(member):
            classes.append(member)
        elif inspect.isfunction(member):
            functions.append(member)
    return classes, functions, sub_modules


def add_structs_to_tree(classes, functions, module, tree_root_node):
    module_path = inspect.getfile(module)
    structs = get_in_module_structs(module, functions, classes)
    process_structs_to_tree(structs, tree_root_node)


def process_structs_to_tree(structs: List[module_struct], root_node):
    section_level_stack = [-1]
    parent_list = [root_node]
    section_nodes = []
    for struct_type, struct_obj, struct_pos in structs:
        curr_parent = parent_list[-1]
        if struct_type == "comment":
            add_comment_struct_to_tree(curr_parent, parent_list, section_level_stack,
                                       section_nodes, struct_obj)
        elif struct_type == "function":
            func_name = struct_obj.__name__
            func_node = {"type": "function", "obj": struct_obj, "name": func_name,
                         "children": {}}
            curr_parent["children"][func_name] = func_node
        elif struct_type == "class":
            class_name = struct_obj.__name__
            class_node = {"type": "class", "obj": struct_obj, "name": class_name,
                          "children": {}}
            curr_parent["children"][class_name] = class_node
            get_class_members(struct_obj, class_node["children"])

    for section_node in section_nodes:
        section_node["obj"] = "\n".join(section_node["obj"])

    return root_node


def process_sub_modules(sub_modules, tree_root_node):
    for i, sub_module in enumerate(sub_modules):
        name = sub_module.__name__.split(".")[-1]
        member = sub_module
        member_path = inspect.getfile(member)
        new_tree_root_node = {"type": "module", "children": {}, "obj": member,
                              "name": name}
        tree_root_node["children"][name] = new_tree_root_node
        get_module_members(member, new_tree_root_node, member_path)


def add_comment_struct_to_tree(curr_parent, parent_list, section_level_stack,
                               section_nodes, struct_obj):
    token_list = struct_obj
    for token_type, token_content, token_pos in token_list:
        if token_type == "section":
            section_title, section_level = token_content
            curr_section_level = section_level_stack[-1]
            section_contents = []
            section_node = {"type": "section", "obj": section_contents,
                            "name": section_title, "children": {}}
            section_nodes.append(section_node)
            curr_parent["children"][section_title] = section_node
            if section_level > curr_section_level:
                section_level_stack.append(section_level)
            elif section_level < curr_section_level:
                while section_level_stack[-1] > section_level:
                    section_level_stack.pop()
                    parent_list.pop()
                section_level_stack.append(section_level)
            else:
                parent_list.pop()
            parent_list.append(section_node)
            curr_parent = section_node
        elif token_type == "text":
            if curr_parent["type"] == "section":
                curr_parent["obj"].append(token_content)
            else:
                curr_parent["children"][token_content] = {"type": "comment",
                                                          "obj": token_content,
                                                          "name": ""}


def get_class_members(cls, tree_root: Dict):
    for name, member in inspect.getmembers(cls):
        if isinstance(member, classmethod):
            continue
        type_str = str(type(member))
        # check whether member is a function
        if type_str == "<class 'function'>":
            tree_root[name] = {"type": "function", "obj": member}
        # Add classmethods
        elif type_str == "<class 'mappingproxy'>":
            for sub_name, sub_member in member.items():
                if isinstance(sub_member, classmethod):
                    tree_root[sub_name] = {"type": "function", "obj": sub_member}


"""
## Build notebook for module from the tree
"""


def build_notebook_for_module(leaf, root_note: Note, docs_parser: Doc_parser):
    child_note = Note(root_note.default_notebook)
    child_key = leaf["type"] + ": " + leaf["name"]
    root_note.add_child(child_key, child_note)
    child_type = "code:" + leaf["type"]
    child_obj = leaf["obj"]
    docs = inspect.getdoc(leaf["obj"])
    child_note.resource.add_resource(child_obj, child_type, docs)

    for name, child in leaf["children"].items():
        docs = {}
        match child["type"]:
            case "function":
                doc_raw = inspect.getdoc(child["obj"])
                if doc_raw is None:
                    docs = " ".join(name.split("_"))
                    general, parameter, return_value, keywords = ("", {}, "", [])
                else:
                    general, parameter, return_value, keywords = docs_parser(doc_raw)
                function_note = child_note.s("function: " + name)
                function_note.be(name)
                function_docs = FunctionDocs(general, parameter, return_value, keywords)
                function_note.resource.add_function(child["obj"], function_docs)
            case "module":
                build_notebook_for_module(child, child_note, docs_parser)
            case "class":
                build_notebook_for_module(child, child_note, docs_parser)
            case "comment":
                child_note.new_child(name).be(child["obj"])
            case "section":
                child_note.be(child["obj"])
                build_notebook_for_module(child, child_note, docs_parser)


if __name__ == "__main__":
    from evonote.testing import v_lab

    notebook = get_notebook_for_module(v_lab)
    notebook.show_notebook_gui()
