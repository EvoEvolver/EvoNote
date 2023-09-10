from typing import List

from evonote.notebook.note import Note
from evonote.notebook.notebook import Notebook


class Bookshelf(Notebook):
    def __init__(self, topic):
        super().__init__(topic)

    def add_notebook_by_path(self, path: List[str], notebook: Notebook):
        note = get_note_for_notebook(notebook, self)
        self.add_note_by_path(path, note)
        return note


def get_note_for_notebook(notebook: Notebook, default_notebook: Notebook) -> Note:
    note = Note(default_notebook)
    note.resource.add_notebook(notebook, notebook.topic)
    note.be("A notebook with topic: " + notebook.topic)
    return note
