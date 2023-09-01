from __future__ import annotations
import ast
from typing import Dict, List, Any

from evonote import EvolverInstance
from evonote.core.notebook import Notebook
from evonote.writer.writer import Writer
from evonote.file_helper.core import delete_old_comment_output
from evonote.file_helper.evolver import get_caller_id


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


def new_notebook_from_note_subset(notes: List[Note], notebook: Notebook) -> Notebook:
    new_notebook = Notebook(topic=notebook.topic)
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
    if topic is None:
        topic = ""
    notebook = Notebook(topic)
    root = Note(default_notebook=notebook)
    notebook.set_root(root)
    return root, notebook
