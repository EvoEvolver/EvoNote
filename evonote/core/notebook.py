from __future__ import annotations

from typing import Dict, List, Type, Callable

import yaml

from evonote.core.note import Note, delete_extra_keys_for_prompt, \
    new_notebook_from_note_subset
from evonote.gui.notebook import draw_treemap
from evonote.indexing.indexing import Indexing, Indexer


class Notebook:
    """
    Store the information of notes contained
    The information is mainly the relationship between notes
    """

    def __init__(self, topic):
        self.children: Dict[Note, Dict[str, Note]] = {}
        self.note_path: Dict[Note, List[str]] = {}
        self.parents: Dict[Note, List[Note]] = {}

        self.indexings: List[Indexing] = []

        self.topic = topic
        self.root: Note | None = None

    def add_indexing(self, indexer_class: Type[Indexer]):
        new_indexing = Indexing(self.get_all_notes(), indexer_class, self)
        self.indexings.append(new_indexing)

    def get_note_path(self, note: Note):
        if note not in self.note_path:
            self.note_path[note] = []
        return self.note_path[note]

    def get_children_dict(self, note: Note):
        if note not in self.children:
            self.children[note] = {}
        return self.children[note]

    def get_parents(self, note: Note):
        if note in self.parents:
            return self.parents[note]
        else:
            raise Exception("No parent found")

    def get_note_by_path(self, path: List[str]) -> Note | None:
        assert self.root is not None
        leaf = self.root
        for key in path:
            leaf = self.children[leaf].get(key, None)
            if leaf is None:
                return None
        return leaf

    def add_note_by_path(self, path: List[str], note: Note) -> Note:
        assert self.root is not None
        leaf = self.root
        for key in path[:-1]:
            children = self.children[leaf]
            if key not in children:
                leaf.add_child(key, Note(self))
            leaf = children[key]
        leaf.add_child(path[-1], note)
        return leaf

    def set_root(self, root: Note):
        self.children[root] = {}
        self.note_path[root] = []
        self.parents[root] = []
        self.root = root

    def get_all_notes(self):
        return list(self.children.keys())

    def add_child(self, key: str, parent: Note, child: Note):
        if child not in self.children:
            self.children[child] = {}
        # ensure the parent is in the tree
        assert parent in self.children
        children_dict = self.get_children_dict(parent)
        children_dict[key] = child
        parent_note_path = self.get_note_path(parent)
        child_note_path = parent_note_path + [key]
        self.note_path[child] = child_note_path
        if child not in self.parents:
            self.parents[child] = [parent]
        else:
            self.parents[child].append(parent)

        for indexing in self.indexings:
            indexing.add_new_note(child)

    def remove_note(self, note: Note):
        """
        Remove a note from the tree
        This will remove all the indexing data of the notebook
        It is better to create another
        :param note:
        :return:
        """
        children_dict = self.get_children_dict(note)
        for key, child in children_dict.items():
            self.remove_note(child)

        parents = self.get_parents(note)
        for parent in parents:
            children_dict = self.get_children_dict(parent)
            for key, child in children_dict.items():
                if child is note:
                    del children_dict[key]
                    break

        del self.children[note]
        del self.note_path[note]
        del self.parents[note]
        for indexing in self.indexings:
            indexing.remove_note(note)

    def get_dict_for_prompt(self):
        tree = {
            "subtopics": {},
        }
        notes = self.get_all_notes()
        note_indexed = []
        i_note = 0
        for i, note in enumerate(notes):
            note_path = self.get_note_path(note)
            leaf = tree
            for key in note_path:
                if key not in leaf["subtopics"]:
                    leaf["subtopics"][key] = {"subtopics": {}}
                leaf = leaf["subtopics"][key]
            if len(note.content) > 0:
                leaf["content"] = note.content
                leaf["index"] = i_note
                note_indexed.append(note)
                i_note += 1
        return tree, note_indexed

    def get_yaml_for_prompt(self):
        tree, note_indexed = self.get_dict_for_prompt()
        delete_extra_keys_for_prompt(tree)
        return yaml.dump(tree), note_indexed

    def show_notebook_gui(self):
        assert self.root is not None
        draw_treemap(self.root, self)
        pass

    def get_notes_by_similarity(self, query_list: List[str],
                                weights: List[float] | None = None,
                                top_k: int = 10,
                                note_filter: Callable[[Note], bool] = None
                                ) -> List[Note]:
        if weights is None:
            weights = [1.0] * len(query_list)
        assert len(query_list) == len(weights)

        # Use the default indexing
        indexing = self.indexings[0]

        top_k_notes = indexing.get_top_k_notes(query_list, weights, top_k, note_filter)

        return top_k_notes

    def get_sub_notebook_by_similarity(self, query_list: List[str],
                                       weights: List[float] | None = None,
                                       top_k: int = 10,
                                       note_filter: Callable[[Note], bool] = None
                                       ) -> Notebook:
        top_k_descendants = self.get_notes_by_similarity(query_list, weights, top_k,
                                                         note_filter)
        new_notebook = new_notebook_from_note_subset(top_k_descendants, self)
        return new_notebook
