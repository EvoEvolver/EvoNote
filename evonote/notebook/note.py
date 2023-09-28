from __future__ import annotations

from copy import copy
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from evonote.notebook.notebook import Notebook


class Note:
    """
    A tree-like data structure that stores notebook
    usually for the direct summary of paragraphs

    The relation of the items are mainly represented by the tree structure
    It is like a book that AI can read

    Notice that Note object can be indexed by embedding vectors because its
    """

    def __init__(self, notebook: Notebook):
        super().__init__()

        # content is string no matter what _content_type is
        self.content: str = ""
        # The root note helps merge two notebook bases
        self.notebook: Notebook = notebook
        # The resource is the data that is indicated by the note
        self.resource: NoteResource = NoteResource()

    def copy_to(self, notebook: Notebook):
        new_note = Note(notebook)
        new_note.content = copy(self.content)
        new_note.resource = copy(self.resource)
        return new_note

    """
    ## Functions for getting the relation of notes
    """

    def get_note_path(self):
        return self.notebook.get_note_path(self)

    def get_parents(self):
        return self.notebook.get_parents(self)

    def get_children(self):
        return self.notebook.get_children_dict(self)

    def has_child(self, key: str):
        return self.notebook.has_child(self, key)

    """
    ## Functions for adding children of note
    """

    def add_child(self, key: str, note) -> Note:
        self.notebook.add_child(key, self, note)
        return note

    def new_child(self, key: str) -> Note:
        note = Note(self.notebook)
        self.notebook.add_child(key, self, note)
        return note

    """
    ## Functions for setting content of note
    """

    def s(self, key) -> Note:
        """
        Creating a new child note or addressing an existing child note
        :param key: the key of the child note
        :return:
        """
        notebook = self.notebook
        if isinstance(key, int) or isinstance(key, str):
            children = notebook.get_children_dict(self)
            if key not in children:
                note = Note(notebook)
                notebook.add_child(key, self, note)
                return note
            return children[key]
        else:
            raise NotImplementedError()

    def set_content(self, content: str) -> Note:
        """
        :return: The note itself
        """
        self.content = content
        return self

    def be(self, content: str) -> Note:
        """
        :return: The note itself
        """
        self.content = content
        return self

    def __str__(self):
        if len(self.content) == 0:
            return "Path" + str(self.get_note_path())
        return self.content

    def __repr__(self):
        return f"<{self.__class__.__name__}> {str(self.get_note_path())}"
    

class NoteResource:
    def __init__(self):
        self.resource = {}
        # Possible types: Notebook, Note, Function, Class, Module
        self.resource_type = {}

    def has_type(self, resource_type):
        return resource_type in self.resource_type.values()

    """
    ## Functions for getting resources
    """

    def get_resource_by_type(self, resource_type):
        """
        Return the first resource of the given type
        """
        for key, value in self.resource_type.items():
            if value == resource_type:
                return self.resource[key]
        return None

    def get_resource_and_docs_by_type(self, resource_type):
        """
        Return the first resource of the given type with its docs
        """
        for i in range(len(self.resource_type)):
            if self.resource_type[i] == resource_type:
                return self.resource[i]
        return None

    def get_resource_types(self):
        return set(self.resource_type.values())

    """
    ## Functions for adding resources
    """

    def add_resource(self, resource, resource_type: str, key: str):
        self.resource[key] = resource
        self.resource_type[key] = resource_type

    def add_text(self, text, key: str):
        self.add_resource(text, "text", key)

    def add_notebook(self, notebook, key: str):
        self.add_resource(notebook, "notebook", key)

    def add_function(self, function, key: str):
        self.add_resource(function, "function", key)

    def add_module(self, module, key: str):
        self.add_resource(module, "module", key)

    def add_class(self, class_, key: str):
        self.add_resource(class_, "class", key)

    def add_note(self, note, key: str):
        self.add_resource(note, "note", key)
