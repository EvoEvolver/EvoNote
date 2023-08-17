from __future__ import annotations
import ast
from typing import Dict, List
from evonote import EvolverInstance
from evonote.file_helper.core import delete_old_comment_output
from evonote.file_helper.evolver import get_caller_id
from evonote.model.llm import get_embeddings
from evonote.core.knowledge import KnowledgeItem
from evonote.core.writer import Writer



class Note(KnowledgeItem):
    """
    A tree-like data structure that stores core
    usually for the direct summary of paragraphs

    The relation of the items are mainly represented by the tree structure
    It is like a book that AI can read

    Notice that Note object can be indexed by embedding vectors because its
    """
    def __init__(self, default_notebook: Notebook):
        super().__init__()

        self._is_note = True
        # _content is string no matter what _content_type is
        self._content: str = ""
        # _content_type helps deserialize _content
        self._content_type = None
        # The root note helps merge two core bases
        self.default_notebook: Notebook = default_notebook

    @property
    def note_path(self):
        return self.get_note_path(self.default_notebook)

    @property
    def parents(self):
        return self.get_parents(self.default_notebook)

    @property
    def children(self):
        return self.get_children(self.default_notebook)

    def get_note_path(self, notebook: Notebook | None = None):
        notebook = notebook if notebook is not None else self.default_notebook
        return notebook.get_note_path(self)

    def get_parents(self, notebook: Notebook | None = None):
        notebook = notebook if notebook is not None else self.default_notebook
        return notebook.get_parents(self)

    def get_children(self, notebook: Notebook | None = None):
        notebook = notebook if notebook is not None else self.default_notebook
        return notebook.get_children_dict(self)

    def add_child(self, key: str, note: Note, notebook: Notebook | None = None):
        notebook = notebook if notebook is not None else self.default_notebook
        notebook.add_child(key, self, note)


    def be(self, writer: Writer | str) -> Note:
        """
        Assign the note with a writer (generator)
        :param writer:
        :return: The note itself
        """
        if isinstance(writer, str):
            self._content = writer
        elif "_is_writer" in writer.__dict__:
            comp_result = writer._get_comp_result(self)
            writer._set_with_comp_result(comp_result, self)
            if len(writer._after_assign) > 0:
                manager, line_i, stacks = EvolverInstance.get_context()
                for func in writer._after_assign:
                    func(self, manager, line_i, stacks)
        return self


    def show(self):
        evolver_id = "show"
        manager, line_i, stacks = EvolverInstance.get_context()
        caller_id = get_caller_id(stacks[0])
        manager.clear_ops_for_caller(caller_id)
        code_line = manager.get_src_line(line_i)
        delete_old_comment_output(manager, caller_id, line_i, evolver_id)
        lines_to_insert = str(self._content).splitlines()
        manager.insert_comment_with_same_indent_after(caller_id, line_i, lines_to_insert,
                                                      evolver_id)

    def __str__(self):
        return self._content

    def __repr__(self):
        res = self.note_path
        return res

    def s(self, key) -> Note:
        """
        Creating a new child note or addressing an existing child note
        :param key: the key of the child note
        :return:
        """
        if isinstance(key, int) or isinstance(key, str):
            if key not in self.children:
                note = Note(self.default_notebook)
                self.add_child(key, note)
                return note
            return self.children[key]
        else:
            raise NotImplementedError()

    def obj(self, index=None):
        """
        Parse the content as an object. Return the object or the value on the index
        :return:
        """
        obj = ast.literal_eval(self._content)
        if index is not None:
            return obj[index]
        return obj

    def line(self, index: int | str, end: str | None = None) -> str:
        lines = str(self).split("\n")
        lines = [line.strip() for line in lines]
        if isinstance(index, int):
            if end is None:
                return lines[index]
            else:
                return "\n".join(lines[index: end])
        else:
            raise NotImplementedError()

    def paragraph(self, index: int | str, end: str | None = None) -> str:
        lines = str(self).split("\n\n")
        lines = [line.strip() for line in lines]
        if isinstance(index, int):
            if end is None:
                return lines[index]
            else:
                return "\n\n".join(lines[index: end])
        else:
            raise NotImplementedError()

    def __getitem__(self, key):
        if isinstance(key, int) or isinstance(key, str):
            if key not in self.children:
                return None
            return self.children[key]
        else:
            raise NotImplementedError()

    def get_descendants(self: Note):
        descendants = []
        for child in self.children.values():
            descendants.append(child)
            descendants.extend(get_descendants_of_note(child))
        return descendants


def get_descendants_of_note(note: Note | Notebook):
    descendants = []
    for child in note.children.values():
        descendants.append(child)
        descendants.extend(get_descendants_of_note(child))
    return descendants


class Notebook:
    def __init__(self, path_born):
        self._path_born = path_born
        self.children: Dict[Note, Dict[str, Note]] = {}
        self.note_path: Dict[Note, List[str]] = {}
        self.parents: Dict[Note, List[Note]] = {}

    def get_note_path(self, note: Note):
        if note not in self.note_path:
            self.note_path[note] = []
        return self.note_path[note]

    def get_children_dict(self, note: Note):
        if note not in self.children:
            self.children[note] = {}
        return self.children[note]

    def get_parents(self, note: Note):
        return self.parents[note]

    def add_child(self, key: str, parent: Note, child: Note):
        children_dict = self.get_children_dict(parent)
        children_dict[key] = child
        parent_note_path = self.get_note_path(parent)
        child_note_path = parent_note_path + [key]
        self.note_path[child] = child_note_path
        if child not in self.parents:
            self.parents[child] = [parent]
        else:
            self.parents[child].append(parent)


def make_root_note():
    _, _, stacks = EvolverInstance.get_context()
    path_born = stacks[0].filename
    notebook = Notebook(path_born)
    return Note(default_notebook=notebook)
