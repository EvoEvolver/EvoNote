from __future__ import annotations
import ast
from typing import Dict, Any, TYPE_CHECKING

from evonote import EvolverInstance
from evonote.file_helper.core import delete_old_comment_output
from evonote.file_helper.evolver import get_caller_id

if TYPE_CHECKING:
    from evonote.core.notebook import Notebook


class Note:
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
        # content is string no matter what _content_type is
        self.content: str = ""
        # _content_type helps deserialize content
        self._content_type = None
        # The root note helps merge two core bases
        self.default_notebook: Notebook = default_notebook

        self.type = "text"

        self.related_info: Dict[str, Any] = {}

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

    def get_descendants(self: Note, notebook: Notebook | None = None):
        notebook = notebook if notebook is not None else self.default_notebook
        return get_descendants(self, notebook)

    def add_child(self, key: str, note: Note, notebook: Notebook | None = None) -> Note:
        notebook = notebook if notebook is not None else self.default_notebook
        notebook.add_child(key, self, note)
        return note

    def be(self, content: str) -> Note:
        """
        Assign the note with a writer (generator)
        :param writer:
        :return: The note itself
        """
        self.content = content
        return self

    def show(self):
        evolver_id = "show"
        manager, line_i, stacks = EvolverInstance.get_context()
        caller_id = get_caller_id(stacks[0])
        manager.clear_ops_for_caller(caller_id)
        code_line = manager.get_src_line(line_i)
        delete_old_comment_output(manager, caller_id, line_i, evolver_id)
        lines_to_insert = str(self.content).splitlines()
        manager.insert_comment_with_same_indent_after(caller_id, line_i, lines_to_insert,
                                                      evolver_id)

    def __str__(self):
        if len(self.content) == 0:
            return "Path" + str(self.note_path)
        return self.content

    def s(self, key, notebook: Notebook | None = None) -> Note:
        """
        Creating a new child note or addressing an existing child note
        :param key: the key of the child note
        :return:
        """
        notebook = notebook if notebook is not None else self.default_notebook
        if isinstance(key, int) or isinstance(key, str):
            children = self.get_children(notebook)
            if key not in children:
                note = Note(notebook)
                notebook.add_child(key, self, note)
                return note
            return children[key]
        else:
            raise NotImplementedError()

    """
    def __getitem__(self, key):
        if isinstance(key, int) or isinstance(key, str):
            if key not in self.children:
                return None
            return self.children[key]
        else:
            raise NotImplementedError()
    """


def get_descendants(note: Note, notebook: Notebook):
    descendants = []
    for child in notebook.children[note].values():
        descendants.append(child)
        descendants.extend(get_descendants(child, notebook))
    return descendants
