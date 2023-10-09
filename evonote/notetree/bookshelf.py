from typing import List

from evonote.notetree import Note
from evonote.notetree import Tree


class Bookshelf(Tree):
    def __init__(self, root_content):
        super().__init__(root_content)

    def add_notetree_by_path(self, path: List[str], notetree: Tree):
        note = get_note_for_notetree(notetree, self)
        self.add_note_by_path(path, note)
        return note


def get_note_for_notetree(notetree: Tree, default_notetree: Tree) -> Note:
    note = Note(default_notetree)
    note.resource.add_notetree(notetree, notetree.topic)
    note.be("A notetree with root_content: " + notetree.topic)
    return note
