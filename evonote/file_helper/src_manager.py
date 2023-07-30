from typing import Optional

from evonote.file_helper.utils import escape_multi_quote

comment_delimiter_len = 5
comment_delimiter = '"' * comment_delimiter_len


class SrcManager:
    def __init__(self, src):
        self.src: str = src
        self.src_list: list[str] = src.splitlines()
        self.curr_list: Optional[list[str]] = self.src_list.copy()
        # The position of the original line in the current list
        # The length of the list is the same as the length of src_list
        self.line_map_to_curr: list[int] = [i for i in range(len(self.src_list))]
        # The position of the current line in the original list
        # The length of the list is the same as the length of curr_list
        # -1 means the line is not in the original list
        self.line_map_to_origin: list[int] = [i for i in range(len(self.curr_list))]
        self.pending_ops = {}

    def add_pending_op(self, caller_id, op, args):
        if caller_id in self.pending_ops.keys():
            self.pending_ops[caller_id].append((op, args))
        else:
            self.pending_ops[caller_id] = [(op, args)]

    def clear_ops_for_caller(self, caller_id):
        self.pending_ops[caller_id] = []

    def apply_pending_ops(self):
        for ops in self.pending_ops.values():
            for op, args in ops:
                op(*args)
        # self.pending_ops = {}

    def get_curr_src(self):
        self.apply_pending_ops()
        no_none_list = []
        for line in self.curr_list:
            if line is not None:
                no_none_list.append(line)
        self.__init__(self.src)
        return "\n".join(no_none_list)

    def get_src_line(self, line_i):
        return self.src_list[line_i]

    def get_indent(self, line_idx_origin: int):
        return len(self.src_list[line_idx_origin]) - len(self.src_list[line_idx_origin].lstrip())

    @property
    def src_len(self):
        return len(self.src_list)

    def del_origin_lines(self, caller_id: str, start_line_origin, end_line_origin):
        """
        :param start_line_origin: this line will be deleted
        :param end_line_origin: this line will also be deleted
        """
        self.add_pending_op(caller_id, self.__del_origin_lines, (start_line_origin, end_line_origin))

    def __del_origin_lines(self, start_line_origin, end_line_origin):
        for i in range(start_line_origin, end_line_origin + 1):
            # set the entry in curr_list to empty
            # won't modify line maps
            self.curr_list[self.line_map_to_curr[i]] = None

    def insert_with_same_indent_after(self, caller_id: str, line_in_origin, lines_to_insert):
        self.add_pending_op(caller_id, self.__insert_with_same_indent_after, (line_in_origin, lines_to_insert))

    def __insert_with_same_indent_after(self, line_in_origin, lines_to_insert):
        indent = self.get_indent(line_in_origin)
        start_in_curr = self.line_map_to_curr[line_in_origin]
        for i, line in enumerate(lines_to_insert):
            self.curr_list.insert(start_in_curr + i + 1, " " * indent + line)
            self.line_map_to_origin.insert(start_in_curr + i + 1, -1)
        # update line_map_to_curr
        for i in range(line_in_origin + 1, len(self.line_map_to_curr)):
            self.line_map_to_curr[i] += len(lines_to_insert)

    def insert_comment_with_same_indent_after(self, caller_id: str, line_in_origin, lines_to_insert, evolver_id):
        self.add_pending_op(caller_id, self.__insert_comment_with_same_indent_after,
                            (line_in_origin, lines_to_insert, evolver_id))

    def __insert_comment_with_same_indent_after(self, line_in_origin, lines_to_insert, evolver_id):
        comment_lines = [comment_delimiter + evolver_id]
        for line in lines_to_insert:
            comment_lines.append(escape_multi_quote(line))
        comment_lines.append(comment_delimiter)
        self.__insert_with_same_indent_after(line_in_origin, comment_lines)


