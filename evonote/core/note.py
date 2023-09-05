from __future__ import annotations
from typing import Dict, Any, TYPE_CHECKING

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
        # The root note helps merge two core bases
        self.default_notebook: Notebook = default_notebook
        # The resource is the data that is indicated by the note
        self.resource: NoteResource = NoteResource()

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


def get_descendants(note: Note, notebook: Notebook):
    descendants = []
    for child in notebook.children[note].values():
        descendants.append(child)
        descendants.extend(get_descendants(child, notebook))
    return descendants


class NoteResource:
    def __init__(self):
        self.resource = []
        # Possible types: Notebook, Note, Function, Class, Module
        self.resource_type = []
        self.resource_docs = []

    def add_resource(self, resource, resource_type, resource_docs):
        self.resource.append(resource)
        self.resource_type.append(resource_type)
        self.resource_docs.append(resource_docs)

    def get_resource_types(self):
        return self.resource_type

    def add_text(self, text, text_docs):
        self.add_resource(text, "text", text_docs)

    def add_notebook(self, notebook, notebook_docs):
        self.add_resource(notebook, "notebook", notebook_docs)

    def add_function(self, function, function_docs):
        self.add_resource(function, "function", function_docs)

    def add_module(self, module, module_docs):
        self.add_resource(module, "module", module_docs)

    def add_class(self, class_, class_docs):
        self.add_resource(class_, "class", class_docs)

    def add_note(self, note, note_docs):
        self.add_resource(note, "note", note_docs)