from __future__ import annotations

import ast

from evonote import EvolverInstance
from evonote.data_type.chat import Chat
from evonote.core.note import Note
from evonote.core.writer import Writer, get_notes_by_linage, \
    default_kwargs_chat_openai, \
    verbose, get_prompt_for_useful_notes, get_nearby_paths_in_prompt
from evonote.model.llm import complete_chat


class BuildFromWriter(Writer):
    def __init__(self, paragraph, caller_path: str):
        self.paragraph = paragraph
        super().__init__("build_from", ["paragraph"], caller_path)

    def _write(self, note: Note) -> str:
        chat = Chat(system_message="""You are a helpful assistant for arranging core to a core base. You should output merely JSON.""")
        chat.add_user_message(self.paragraph)
        chat.add_user_message("""Summarize the above paragraph into a tree. Give the result in JSON with the keys being "subject", "statement", "subtopics".""")
        res = complete_chat(chat, default_kwargs_chat_openai)
        try:
            parsed_res = ast.literal_eval(res)
        except:
            raise Exception("Parse failed")

        return res

    def _set_with_comp_result(self, comp_result, note: Note):
        parsed_res = ast.literal_eval(comp_result)
        iter_and_assign(note, parsed_res)

def iter_and_assign(note: Note, tree: dict):
    if "subject" not in tree or "statement" not in tree:
        raise Exception("incomplete tree node")
        return
    node = note.s(tree["subject"]).be(tree["statement"])
    if "subtopics" not in tree:
        return
    for subtopic in tree["subtopics"]:
        iter_and_assign(node, subtopic)



def build_from(paragraph: str) -> Writer:
    _, _, stack = EvolverInstance.get_context()
    return BuildFromWriter(paragraph, stack[0].filename)
