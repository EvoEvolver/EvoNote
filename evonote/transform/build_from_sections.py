from __future__ import annotations

import ast
import concurrent.futures

from evonote.data_cleaning.document import Document
from evonote.file_helper.cache_manage import save_cache, cached_function
from evonote.model.chat import Chat
from evonote.mindtree import Note
from evonote.mindtree import Tree


def mindtree_from_doc(doc: Document, meta) -> Tree:
    mindtree = Tree(meta["title"])
    build_from_sections(doc, mindtree.root)
    return mindtree


def build_from_sections(doc: Document, root: Note):
    root.be(doc.content)
    for section in doc.sections:
        build_from_sections(section, root.s(section.title))


def move_original_content_to_resource(note, mindtree):
    new_note = Note(mindtree)
    if len(note.content) > 0:
        new_note.resource.add_text(note.content, "original_content")
    return new_note


def digest_all_descendants(mindtree: Tree) -> Tree:
    mindtree = mindtree.duplicate_tree_by_note_mapping(
        move_original_content_to_resource)
    all_notes = mindtree.get_note_list()
    contents = [note.resource.get_resource_by_type("text") for note in all_notes]
    non_empty_contents = []
    non_empty_notes = []
    for i in range(len(contents)):
        if contents[i] is not None:
            non_empty_contents.append(contents[i])
            non_empty_notes.append(all_notes[i])
    finished = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        for note, digest in zip(non_empty_notes, executor.map(digest_content,
                                                              non_empty_contents)):
            note: Note
            set_notes_by_digest(note, digest)
            finished += 1
        if finished % 5 == 4:
            print("digest received ", finished, "/", len(all_notes))
            save_cache()
    save_cache()
    return mindtree

@cached_function("digest_content")
def digest_content(content):

    chat = Chat(
        system_message="""You are a helpful assistant for arranging knowledge. You should output merely JSON.""")
    chat.add_user_message(content)
    chat.add_user_message(
        """Summarize the below paragraphs into a tree. Give the result in JSON with the keys being "root_content", "statement", "subtopics". The "statement" entry should be a shortened version of original text.""")

    res = chat.complete_chat()
    if res[0] == "`":
        lines = res.split("\n")
        lines = lines[1:-1]
        res = "\n".join(lines)
    try:
        parsed_res = ast.literal_eval(res)
    except:
        print("failed to parse, retrying...")
        print(res)
        return digest_content(content)

    return res


def set_notes_by_digest(note: Note, digest: str):
    parsed_res = ast.literal_eval(digest)
    iter_and_assign(note, parsed_res)


def iter_and_assign(note: Note, tree: dict):
    if "root_content" not in tree or "statement" not in tree:
        raise Exception("incomplete tree node")
    node = note.s(tree["root_content"]).be(tree["statement"])
    if "subtopics" not in tree:
        return
    for subtopic in tree["subtopics"]:
        iter_and_assign(node, subtopic)
