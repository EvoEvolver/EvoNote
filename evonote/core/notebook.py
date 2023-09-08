from __future__ import annotations

from typing import Dict, List, Type, Callable

from evonote.core.note import Note
from evonote.gui.notebook import draw_treemap
from evonote.indexing.core import Indexing, Indexer

from evonote.indexing.core import FragmentedEmbeddingIndexer


class Notebook:
    """
    Store the information of notes contained
    The information is mainly the path of each note
    The indexings of each note
    """

    def __init__(self, topic, root: Note = None, rule_of_path: str = None):
        """
        :param topic: The topic of the notebook
        :param root: The root of the notebook. If None, a new root will be created
        :param rule_of_path: The rule for creating paths.
        """
        self.children: Dict[Note, Dict[str, Note]] = {}
        self.note_path: Dict[Note, List[str]] = {}
        self.parents: Dict[Note, List[Note]] = {}

        self.indexings: Dict[Type[Indexer], Indexing] = {}

        self.topic = topic
        self.root: Note
        if root is None:
            root = Note(self)
            root.be(topic)
        self.set_root(root)

        self.rule_of_path = rule_of_path

    def add_indexing(self, indexer_class: Type[Indexer]) -> Indexing:
        new_indexing = Indexing(self.get_all_notes(), indexer_class, self)
        self.indexings[indexer_class] = new_indexing
        return new_indexing

    def get_indexing(self, indexer_class: Type[Indexer]) -> Indexing:
        if indexer_class is None:
            indexer_class = FragmentedEmbeddingIndexer
        if indexer_class not in self.indexings:
            return self.add_indexing(indexer_class)
        else:
            return self.indexings[indexer_class]

    def add_simple_indexing(self):
        self.add_indexing(FragmentedEmbeddingIndexer)

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
        if self.root is None:
            self.set_root(Note(self))
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

        for indexing in self.indexings.values():
            indexing.add_new_note(child)

    def remove_note(self, note: Note):
        """
        Remove a note from the tree
        This will remove all the indexing data of the notebook
        It is better to create another notebook that removing a note
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
        for indexing in self.indexings.values():
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

    def get_tree_with_indices_for_prompt(self):
        tree_with_indices, note_indexed = self.get_dict_for_prompt()
        delete_extra_keys_for_prompt(tree_with_indices)
        return tree_with_indices, note_indexed

    def show_notebook_gui(self):
        """
        Show the notebook in a webpage
        """
        assert self.root is not None
        draw_treemap(self.root, self)

    def get_notes_by_similarity(self, query_list: List[str],
                                weights: List[float] | None = None,
                                top_k: int = 10,
                                note_filter: Callable[[Note], bool] = None,
                                indexer_class: Type[Indexer] = None
                                ) -> List[Note]:
        if weights is None:
            weights = [1.0] * len(query_list)
        assert len(query_list) == len(weights)


        indexing = self.get_indexing(indexer_class)

        top_k_notes = indexing.get_top_k_notes(query_list, weights, top_k, note_filter)

        return top_k_notes

    def get_sub_notebook_by_similarity(self, query_list: List[str],
                                       weights: List[float] | None = None,
                                       top_k: int = 10,
                                       note_filter: Callable[[Note], bool] = None,
                                       indexer_class: Type[Indexer] = None
                                       ) -> Notebook:
        top_k_descendants = self.get_notes_by_similarity(query_list, weights, top_k,
                                                         note_filter, indexer_class)
        new_notebook = new_notebook_from_note_subset(top_k_descendants, self)
        return new_notebook

    def duplicate_notebook_by_note_mapping(self, note_mapping: Callable[[Note, Notebook], Note]) -> Notebook:
        """
        Duplicate the notebook by mapping each note to a new note
        It can also be used for creating a copy of the notebook
        :param note_mapping: The mapping function for each note
        :return: A new notebook
        """
        new_notebook = Notebook(self.topic, rule_of_path=self.rule_of_path)
        new_notebook.set_root(note_mapping(self.root, new_notebook))
        for note in self.get_all_notes():
            if note is not self.root:
                # Here is not tested
                new_notebook.add_note_by_path(self.get_note_path(note), note_mapping(note, new_notebook))
        return new_notebook


def make_notebook_root(topic: str = None) -> tuple[Note, Notebook]:
    if topic is None:
        topic = ""
    notebook = Notebook(topic)
    return notebook.root, notebook


def new_notebook_from_note_subset(notes: List[Note], notebook: Notebook) -> Notebook:
    new_notebook = Notebook(topic=notebook.topic, root=notebook.root)
    root = new_notebook.root
    for note in notes:
        leaf = root
        note_path = note.get_note_path(notebook)
        for key in note_path[:-1]:
            children = leaf.get_children(notebook=new_notebook)
            if key not in children:
                leaf.add_child(key, notebook.get_children_dict(leaf)[key], new_notebook)
            leaf = children[key]
        leaf.add_child(note_path[-1], note, new_notebook)
    return new_notebook


def delete_extra_keys_for_prompt(tree):
    for key, leaf in tree["subtopics"].items():
        delete_extra_keys_for_prompt(leaf)
    if "content" not in tree:
        for key, leaf in tree["subtopics"].items():
            tree[key] = leaf
        del tree["subtopics"]
    else:
        if len(tree["subtopics"]) == 0:
            del tree["subtopics"]
        if len(tree["content"]) == 0:
            del tree["content"]
