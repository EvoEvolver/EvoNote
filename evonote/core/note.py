from __future__ import annotations
import ast
from typing import Dict, List, Any, Callable, Type

import yaml

from evonote import EvolverInstance
from evonote.core.indexing.indexing import Indexing, Indexer
from evonote.core.visualize import draw_treemap
from evonote.file_helper.core import delete_old_comment_output
from evonote.file_helper.evolver import get_caller_id
from evonote.core.writer import Writer


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

    def index_descendants(self, notebook: Notebook | None = None):
        notebook = notebook if notebook is not None else self.default_notebook
        descendants = get_descendants(self, notebook)
        indexers = [notebook.get_indexer(descendant) for descendant in descendants]
        vectors, vector_index_to_descendants = notebook.indexer_class.get_vectors(
            indexers)
        notebook.descendant_indexing[self] = {"vectors": vectors,
                                              "vector_index_to_descendants": vector_index_to_descendants,
                                              "descendants": descendants}
        return

    def match_descendants(self, query_list: List[str], weights: List[float] | None = None,
                          notebook: Notebook | None = None, top_k: int = 10):
        notebook = notebook if notebook is not None else self.default_notebook
        weights = weights if weights is not None else [1.0] * len(query_list)
        if self not in notebook.descendant_indexing:
            self.index_descendants(notebook)
        vectors = notebook.descendant_indexing[self]["vectors"]
        vector_index_to_descendants = notebook.descendant_indexing[self][
            "vector_index_to_descendants"]
        similarity = notebook.indexer_class.get_similarities(query_list, vectors, weights)
        top_k_indices = similarity.argsort()[-top_k:][::-1]
        descendants = notebook.descendant_indexing[self]["descendants"]
        top_k_descendants = [descendants[vector_index_to_descendants[index]] for index in
                             top_k_indices]
        return top_k_descendants

    def new_notebook_by_match_descendants(self, query_list: List[str],
                                          weights: List[float] | None = None,
                                          notebook: Notebook | None = None,
                                          top_k: int = 10):
        notebook = notebook if notebook is not None else self.default_notebook
        top_k_descendants = self.match_descendants(query_list, weights, notebook, top_k)
        # Make a new notebook
        new_notebook = new_notebook_from_note_subset(top_k_descendants, notebook)
        return new_notebook

    def be(self, writer: Writer | str) -> Note:
        """
        Assign the note with a writer (generator)
        :param writer:
        :return: The note itself
        """
        if isinstance(writer, str):
            self.content = writer
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
        lines_to_insert = str(self.content).splitlines()
        manager.insert_comment_with_same_indent_after(caller_id, line_i, lines_to_insert,
                                                      evolver_id)

    def __str__(self):
        if len(self.content) == 0:
            return "Path" + str(self.note_path)
        return self.content

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
        obj = ast.literal_eval(self.content)
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


def get_descendants_of_note(note: Note | Notebook):
    descendants = []
    for child in note.children.values():
        descendants.append(child)
        descendants.extend(get_descendants_of_note(child))
    return descendants




class Notebook:
    """
    Store the information of notes contained
    The information is mainly the relationship between notes
    """

    def __init__(self, topic, path_born):
        self.path_born = path_born
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


def new_notebook_from_note_subset(notes: List[Note], notebook: Notebook) -> Notebook:
    new_notebook = Notebook(topic=notebook.topic, path_born=notebook.path_born)
    new_notebook.root = notebook.root
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


def get_descendants(note: Note, notebook: Notebook):
    descendants = []
    for child in notebook.children[note].values():
        descendants.append(child)
        descendants.extend(get_descendants(child, notebook))
    return descendants


def make_notebook_root(topic: str = None) -> tuple[Note, Notebook]:
    path_born = EvolverInstance.get_caller_path()
    if topic is None:
        topic = ""
    notebook = Notebook(topic, path_born)
    root = Note(default_notebook=notebook)
    notebook.set_root(root)
    return root, notebook
