from __future__ import annotations

import ast

from evonote import EvolverInstance
from evonote.data_type.chat import Chat
from evonote.core.note import Note
from evonote.core.writer import Writer, default_kwargs_chat_openai
from evonote.model.llm import complete_chat


class BuildFromWriter(Writer):
    def __init__(self, paragraph, caller_path: str):
        self.paragraph = paragraph
        super().__init__("build_from", ["paragraph"], caller_path)

    def _write(self, note: Note) -> str:
        return digest_content(self.paragraph)

    def _set_with_comp_result(self, comp_result, note: Note):
        set_notes_by_digest(note, comp_result)

def digest_content(content, use_cache=False, caller_path=None):
    if caller_path is None:
        _, _, stack = EvolverInstance.get_context()
        caller_path = stack[0].filename
    cache = EvolverInstance.read_cache(content, "digest_content",
                                       caller_path, True)
    if use_cache:
        if cache.is_valid():
            return cache._value

    chat = Chat(
        system_message="""You are a helpful assistant for arranging knowledge. You should output merely JSON.""")
    chat.add_user_message(content)
    chat.add_user_message(
        """Summarize the below paragraphs into a tree. Give the result in JSON with the keys being "topic", "statement", "subtopics". The "statement" entry should be a shortened version of original text.""")

    res = complete_chat(chat, default_kwargs_chat_openai)
    if res[0] == "`":
        lines = res.split("\n")
        lines = lines[1:-1]
        res = "\n".join(lines)
    try:
        parsed_res = ast.literal_eval(res)
    except:
        print("failed to parse, retrying...")
        print(res)
        return digest_content(content, use_cache, caller_path)

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


def build_from(paragraph: str) -> Writer:
    _, _, stack = EvolverInstance.get_context()
    return BuildFromWriter(paragraph, stack[0].filename)
