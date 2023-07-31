from __future__ import annotations
import ast
from typing import Dict
from evonote import EvolverInstance
from evonote.file_helper.core import delete_old_comment_output
from evonote.file_helper.evolver import get_caller_id
from evonote.model.llm import get_embeddings
from evonote.core.knowledge import KnowledgeItem, RootKnowledgeItem
from evonote.core.writer import Writer



class Note(KnowledgeItem):
    """
    A tree-like data structure that stores core
    usually for the direct summary of paragraphs

    The relation of the items are mainly represented by the tree structure
    It is like a book that AI can read
    """
    def __init__(self):
        super().__init__()

        self._is_note = True
        # _note_path looks like /a/b/c
        self._note_path: str = ""
        # _content is string no matter what _content_type is
        self._content: str = ""
        # _content_type helps deserialize _content
        self._content_type = None

        self._children: Dict[str, Note] = {}
        # The root note helps merge two core bases
        self._root: Notebook | None = None

        # The parents of this note
        self._parents = None
        # The related notes of this note
        # crawling through the related notes can help us find the relevant notes
        self._related_notes = []

    def be(self, writer: Writer | str) -> Note:
        """
        Assign the note with a writer (generator)
        :param writer:
        :return: The note itself
        """
        if isinstance(writer, str):
            self._content = writer
        elif "_is_writer" in writer.__dict__:
            comp_result = writer._get_comp_result(self)
            writer._set_with_comp_result(comp_result, self)
            if len(writer._after_assign) > 0:
                manager, line_i, stacks = EvolverInstance.get_context()
                for func in writer._after_assign:
                    func(self, manager, line_i, stacks)
        return self

    def cite(self, note: Note, *args) -> Note:
        """
        Adding related notes to the note
        Usage: note.cite(note1, note2, ...)
        :return:
        """
        self._related_notes.append(note)
        self._related_notes.extend(args)
        return self

    def next_index(self):
        i = 0
        while str(i) in self._children:
            i += 1
        return self.s(str(i))

    def show(self):
        evolver_id = "show"
        manager, line_i, stacks = EvolverInstance.get_context()
        caller_id = get_caller_id(stacks[0])
        manager.clear_ops_for_caller(caller_id)
        code_line = manager.get_src_line(line_i)
        delete_old_comment_output(manager, caller_id, line_i, evolver_id)
        lines_to_insert = str(self._content).splitlines()
        manager.insert_comment_with_same_indent_after(caller_id, line_i, lines_to_insert,
                                                      evolver_id)

    def __str__(self):
        return self._content

    def __repr__(self):
        res = self._note_path
        return res

    def s(self, key) -> Note:
        """
        Creating a new child note or addressing an existing child note
        :param key: the key of the child note
        :return:
        """
        if isinstance(key, int) or isinstance(key, str):
            if key not in self._children:
                return init_child_note(self, key)
            return self._children[key]
        else:
            raise NotImplementedError()

    def obj(self, index=None):
        """
        Parse the content as an object. Return the object or the value on the index
        :return:
        """
        obj = ast.literal_eval(self._content)
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
            if key not in self._children:
                return None
            return self._children[key]
        else:
            raise NotImplementedError()


#def get_relevance_score(note: Note, query_vector: np.ndarray):


def get_all_descendants(note: Note | Notebook):
    descendants = []
    for child in note._children.values():
        descendants.append(child)
        descendants.extend(get_all_descendants(child))
    return descendants

def get_children_and_embeddings(note: Note):
    children = get_all_descendants(note)
    children_with_content = [child for child in children if len(child._content) > 0]
    children_content = [child._content for child in children_with_content]
    embeddings = get_embeddings(children_content)
    for i, child in enumerate(children_with_content):
        child._tag_keys["content"] = children_content[i]
        child._attention_vectors["content"] = embeddings[i]
    return children_with_content, embeddings


class Notebook(RootKnowledgeItem):
    def __init__(self, path_born):
        super().__init__()
        self._note_path = ""
        self._root = self
        self._path_born = path_born
        self._is_root = True
        self._children: Dict[str, Note] = {}

    def get_items(self):
        return get_all_descendants(self)


def init_child_note(note: Note, key: str):
    child = Note()
    child._note_path = note._note_path + "/" + key if len(note._note_path) > 0 else key
    note._children[key] = child
    child._parents = note
    child._root = note._root
    return child


def make_root_note():
    _, _, stacks = EvolverInstance.get_context()
    path_born = stacks[0].filename
    note = Notebook(path_born)
    return note