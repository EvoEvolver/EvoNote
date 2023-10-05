from __future__ import annotations

from typing import Dict, List, Type, Callable, Tuple

import dill
from bidict import bidict

from evonote.gui.notebook import draw_treemap
from evonote.indexing.core import FragmentedEmbeddingIndexer
from evonote.indexing.core import Indexing, Indexer
from evonote.notebook.note import Note


class Notebook:
    """
    Store the information of notes contained
    The information is mainly the path of each note
    The indexings of each note
    """

    n_notebook = 0

    def __init__(self, topic, rule_of_path: str = None):
        """
        :param topic: The topic of the notebook
        :param rule_of_path: The rule for creating paths.
        """
        self.children: Dict[Note, Dict[str, Note]] = {}
        self.note_path: bidict[Note, Tuple[str]] = bidict()

        # The dict for indexings made for the notebook
        # The key is the class of the indexer and the value is the indexing
        # The reason for using class as key is that the class is more static and hashable
        self.indexings: Dict[Type[Indexer], Indexing] = {}

        self.topic = topic

        # Set up the root
        root = Note(self)
        self.children[root] = {}
        self.note_path[root] = tuple()

        self.rule_of_path = rule_of_path

        self.in_prompt_name = "#" + str(Notebook.n_notebook)
        Notebook.n_notebook += 1

    """
    ## Indexing of notes
    """

    def make_indexing(self, indexer_class: Type[Indexer]) -> Indexing:
        if indexer_class is None:
            indexer_class = FragmentedEmbeddingIndexer
        if indexer_class not in self.indexings:
            new_indexing = Indexing(self.get_all_notes(), indexer_class, self)
            self.indexings[indexer_class] = new_indexing
            return new_indexing
        else:
            return self.indexings[indexer_class]

    """
    ## Note information query
    """

    def get_note_path(self, note: Note):
        return self.note_path[note]

    def get_children_dict(self, note: Note):
        return self.children[note]

    def get_parent(self, note: Note):
        note_path = self.get_note_path(note)
        if len(note_path) == 0:
            return None
        parent_path = note_path[:-1]
        parent = self.get_note_by_path(parent_path)
        return parent

    def has_child(self, note: Note, key: str):
        return key in self.get_children_dict(note)

    @property
    def root(self):
        root = self.get_note_by_path(tuple())
        return root

    """
    ## Note operations
    """

    def set_root(self, note: Note):
        if self.root in self.children:
            children = self.children[self.root]
        else:
            children = {}
        self.children[note] = children
        del self.note_path[self.root]
        self.note_path[note] = tuple()


    def get_note_by_path(self, path: Tuple | List) -> Note | None:
        path = tuple(path)
        return self.note_path.inverse[path]

    def add_note_by_path(self, path: Tuple[str] | List[str], note: Note | str) -> Note:
        if isinstance(note, str):
            note_content = note
            note = Note(self)
            note.set_content(note_content)
        note: Note
        if len(path) == 0:
            self.set_root(note)
            return note
        leaf = self.root
        for key in path[:-1]:
            children = self.children[leaf]
            if key not in children:
                self.add_child(key, leaf, Note(self))
            leaf = children[key]
        self.add_child(path[-1], leaf, note)
        return note

    def get_new_note_by_path(self, path: List[str]) -> Note:
        new_note = Note(self)
        self.add_note_by_path(path, new_note)
        return new_note

    def get_all_notes(self):
        return list(self.children.keys())

    def add_child(self, key: str, parent: Note, child: Note):
        if child.notebook is not self:
            child = child.copy_to(self)
        if child not in self.children:
            self.children[child] = {}
        # ensure the parent is in the tree
        assert parent in self.children
        children_dict = self.get_children_dict(parent)
        children_dict[key] = child
        parent_note_path = self.get_note_path(parent)
        child_note_path = parent_note_path + (key,)
        self.note_path[child] = child_note_path

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

        parent = self.get_parent(note)
        children_dict = self.get_children_dict(parent)
        for key, child in children_dict.items():
            if child is note:
                del children_dict[key]
                break

        del self.children[note]
        del self.note_path[note]
        for indexing in self.indexings.values():
            indexing.remove_note(note)

    """
    ## Representation of notebook in prompt
    """

    def get_notebook_dict(self, add_index=True):
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
                if add_index:
                    leaf["index"] = i_note
                note_indexed.append(note)
                i_note += 1
        return tree, note_indexed

    def get_dict_for_prompt(self):
        dict_without_indices, note_indexed = self.get_notebook_dict(add_index=False)
        delete_extra_keys_for_prompt(dict_without_indices)
        return dict_without_indices

    def get_path_content_str_for_prompt(self):
        res = []
        for note, path in self.note_path.items():
            if len(note.content) == 0:
                continue
            path_str = "/".join(path)
            if len(path) == 0:
                path_str = "root"
            res.append(f"{path_str}: {note.content}")
        return "\n".join(res)

    def get_dict_with_indices_for_prompt(self):
        dict_with_indices, note_indexed = self.get_notebook_dict()
        delete_extra_keys_for_prompt(dict_with_indices)
        return dict_with_indices, note_indexed

    """
    ## Visualization of notebook
    """

    def show_notebook_gui(self):
        """
        Show the notebook in a webpage
        """
        draw_treemap(self.root)

    """
    ## Sub-notebook extraction
    """

    def get_notes_by_similarity(self, query_list: List[str],
                                weights: List[float] | None = None,
                                top_k: int = 10,
                                note_filter: Callable[[Note], bool] = None,
                                indexer_class: Type[Indexer] = None
                                ) -> List[Note]:
        if weights is None:
            weights = [1.0] * len(query_list)
        assert len(query_list) == len(weights)

        indexing = self.make_indexing(indexer_class)

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

    def duplicate_notebook_by_note_mapping(self, note_mapping: Callable[
        [Note, Notebook], Note]) -> Notebook:
        """
        Duplicate the notebook by mapping each note to a new note
        It can also be used for creating a copy of the notebook
        :param note_mapping: The mapping function for each note
        :return: A new notebook
        """
        new_notebook = Notebook(self.topic, rule_of_path=self.rule_of_path)
        for note in self.get_all_notes():
            new_notebook.add_note_by_path(self.get_note_path(note),
                                              note_mapping(note, new_notebook))
        return new_notebook

    """
    ## Persistence of the notebook
    """

    def save(self, path: str, save_indexing: bool = False):
        # TODO: We need to test this function and make sure it works
        with open(path, "wb") as f:
            if not save_indexing:
                indexings = self.indexings
                self.indexings = {}
            try:
                dill.dump(self, f)
            except Exception as e:
                print(e)
            finally:
                if not save_indexing:
                    self.indexings = indexings

    @staticmethod
    def load(path: str) -> Notebook:
        # TODO: We need to test this function and make sure it works
        with open(path, "rb") as f:
            notebook = dill.load(f)
        return notebook

    def __repr__(self):
        return f"<{self.__class__.__name__}> {self.root.content!r}"


def make_notebook_root(topic: str = None) -> tuple[Note, Notebook]:
    if topic is None:
        topic = ""
    notebook = Notebook(topic)
    return notebook.root, notebook


def new_notebook_from_note_subset(notes: List[Note], notebook: Notebook) -> Notebook:
    new_notebook = Notebook(topic=notebook.topic)
    root = new_notebook.root
    for note in notes:
        leaf = root
        note_path = notebook.get_note_path(note)
        for key in note_path[:-1]:
            children_dict = new_notebook.get_children_dict(leaf)
            if key not in children_dict:
                new_notebook.add_child(key, leaf, notebook.get_children_dict(leaf)[key])
            leaf = children_dict[key]
        new_notebook.add_child(note_path[-1], leaf, note)
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
