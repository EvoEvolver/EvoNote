from __future__ import annotations

import ast

from evonote import EvolverInstance
from evonote.core.note import Note
from evonote.core.notebook import Notebook, make_notebook_root
from evonote.model.chat import Chat
import concurrent.futures
from evonote.file_helper.evolver import save_cache


def notebook_from_doc(doc, meta) -> Notebook:
    root, notebook = make_notebook_root(meta["title"])
    build_from_sections(doc, root)
    root.related_info["annotation"] = "This is a notebook of the paper \"" + meta[
        "title"] + "\"."
    return notebook


def build_from_sections(doc, root: Note):
    root.be(doc["content"])
    for section in doc["sections"]:
        build_from_sections(section, root.s(section["title"]))


def digest_all_descendants(notebook: Notebook):
    all_notes = notebook.get_all_notes()
    all_notes = [note for note in all_notes if len(note.content) > 0]
    # digests = []
    digest_content_with_cache = lambda x: digest_content(x, use_cache=True)
    finished = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        for note, digest in zip(all_notes, executor.map(digest_content_with_cache,
                                                        [note.content for note in
                                                         all_notes])):
            # digests.append(digest)
            set_notes_by_digest(note, digest)
            note.related_info["original text"] = note.content
            note.content = ""
            finished += 1
        if finished % 5 == 4:
            print("digest received ", finished, "/", len(all_notes))
            save_cache()
    save_cache()


def digest_content(content, use_cache=False):
    cache = EvolverInstance.read_cache(content, "digest_content")
    if use_cache and cache.is_valid():
        return cache._value

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
        return digest_content(content, use_cache)

    cache.set_cache(res)
    return res


def set_notes_by_digest(note: Note, digest: str):
    parsed_res = ast.literal_eval(digest)
    iter_and_assign(note, parsed_res)


def iter_and_assign(note: Note, tree: dict):
    if "topic" not in tree or "statement" not in tree:
        raise Exception("incomplete tree node")
        return
    node = note.s(tree["topic"]).be(tree["statement"])
    if "subtopics" not in tree:
        return
    for subtopic in tree["subtopics"]:
        iter_and_assign(node, subtopic)
