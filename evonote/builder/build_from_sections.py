from __future__ import annotations

import ast

from evonote.notebook.note import Note
from evonote.notebook.notebook import Notebook, make_notebook_root
from evonote.model.chat import Chat
import concurrent.futures
from evonote.file_helper.cache_manage import save_cache, cache_manager


def notebook_from_doc(doc, meta) -> Notebook:
    root, notebook = make_notebook_root(meta["title"])
    build_from_sections(doc, root)
    return notebook


def build_from_sections(doc, root: Note):
    root.be(doc["content"])
    for section in doc["sections"]:
        build_from_sections(section, root.s(section["title"]))

def move_original_content_to_resource(note, notebook):
    new_note = Note(notebook)
    if len(note.content) > 0:
        new_note.resource.add_text(note.content, "original_content")
    return new_note

def digest_all_descendants(notebook: Notebook) -> Notebook:
    notebook = notebook.duplicate_notebook_by_note_mapping(move_original_content_to_resource)
    all_notes = notebook.get_all_notes()
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
            set_notes_by_digest(note, digest, notebook)
            finished += 1
        if finished % 5 == 4:
            print("digest received ", finished, "/", len(all_notes))
            save_cache()
    save_cache()
    return notebook


def digest_content(content):
    cache = cache_manager.read_cache(content, "digest_content")
    if cache.is_valid():
        return cache.value

    chat = Chat(
        system_message="""You are a helpful assistant for arranging knowledge. You should output merely JSON.""")
    chat.add_user_message(content)
    chat.add_user_message(
        """Summarize the below paragraphs into a tree. Give the result in JSON with the keys being "topic", "statement", "subtopics". The "statement" entry should be a shortened version of original text.""")

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

    cache.set_cache(res)
    return res


def set_notes_by_digest(note: Note, digest: str, notebook):
    parsed_res = ast.literal_eval(digest)
    iter_and_assign(note, parsed_res, notebook)


def iter_and_assign(note: Note, tree: dict, notebook: Notebook):
    if "topic" not in tree or "statement" not in tree:
        raise Exception("incomplete tree node")
        return
    node = note.s(tree["topic"], notebook).be(tree["statement"])
    if "subtopics" not in tree:
        return
    for subtopic in tree["subtopics"]:
        iter_and_assign(node, subtopic, notebook)
