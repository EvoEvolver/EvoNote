from __future__ import annotations

import re
from typing import List

from doc_in_py import Struct

"""
This module is for parse and extract comments
"""

# three_quote_pattern is multi-line comment pattern
three_quote_pattern = re.compile(r'(^|\n)\s*?"""([^(""")]*?)"""', re.DOTALL)


def prepare_raw_comment_struct(parent_src: str) -> List[Struct]:
    min_pos_for_line = get_min_pos_for_line(parent_src)
    min_line_no = 1
    comment_struct_list = []
    matches = three_quote_pattern.finditer(parent_src)
    for match in matches:
        comment_content = match.group(2)
        start = match.group(1)
        start_pos, end_pos = match.span()
        start_pos += len(start)
        start_line_no = find_line_no(start_pos, min_line_no, min_pos_for_line)
        end_line_no = find_line_no(end_pos, start_line_no, min_pos_for_line)
        min_line_no = end_line_no
        comment_pos = (start_line_no, end_line_no)
        comment_struct_list.append(Struct("raw_comment", comment_content, comment_pos))
    return comment_struct_list

def get_min_pos_for_line(src: str) -> List[int]:
    src_lines = src.split("\n")
    min_pos_for_line = [0]
    for line in src_lines:
        min_pos_for_line.append(min_pos_for_line[-1] + len(line) + 1)
    return min_pos_for_line

def find_line_no(pos: int, min_line_no, min_pos_for_line: List[int]) -> int:
    for i in range(min_line_no - 1, len(min_pos_for_line)):
        if pos < min_pos_for_line[i]:
            return i


section_pattern = re.compile(r"(\n\s*?#+ .*)")


def parse_raw_comments(root_struct: Struct):
    new_children = []
    for i, struct in enumerate(root_struct.children):
        if struct.struct_type == "raw_comment":
            comment_content = struct.obj
            comment_structs = process_raw_comment_content(comment_content)
            new_children.extend(comment_structs)
        else:
            new_children.append(struct)
            if struct.struct_type == "class":
                parse_raw_comments(struct)
    root_struct.children = new_children


def process_raw_comment_content(comment_content: str) -> List[Struct]:
    min_pos_for_line = get_min_pos_for_line(comment_content)
    min_line_no = 1

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
        start_line_no = find_line_no(section_start, min_line_no, min_pos_for_line)
        end_line_no = find_line_no(section_end, start_line_no, min_pos_for_line)
        min_line_no = end_line_no
        comment_text_before_section = comment_content[last_section_end+1:section_start]
        last_section_end = section_end
        if len(comment_text_before_section) > 0:
            comment_tokens.append(
                Struct("comment", comment_text_before_section, (0, start_line_no)))
        comment_tokens.append(
            Struct("section", (section_title, section_level),
                   (start_line_no, end_line_no)))
    if last_section_end < len(comment_content):
        remaining_text = comment_content[last_section_end:].strip()
        if len(remaining_text) > 0:
            last_section_end_line_no = find_line_no(last_section_end, min_line_no, min_pos_for_line)
            comment_tokens.append(Struct("comment", remaining_text,
                                         (last_section_end_line_no, len(min_pos_for_line)-1)))
    return comment_tokens
