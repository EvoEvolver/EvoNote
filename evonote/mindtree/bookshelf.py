from typing import List

from evonote.mindtree import Note
from evonote.mindtree import Tree


class Bookshelf(Tree):
    def __init__(self, root_content):
        super().__init__(root_content)

    def add_mindtree_by_path(self, path: List[str], tree: Tree):
        note = get_note_for_mindtree(tree, self)
        self.add_note_by_path(path, note)
        return note


def get_note_for_mindtree(tree: Tree, default_tree: Tree) -> Note:
    note = Note(default_tree)
    note.resource.add_tree(tree, tree.topic)
    note.be("A tree with root_content: " + tree.topic)
    return note
