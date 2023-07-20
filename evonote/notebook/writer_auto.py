from __future__ import annotations

from evonote import EvolverInstance
from evonote.data_type.chat import Chat
from evonote.notebook.notebook import Note
from evonote.notebook.writer import Writer, get_notes_by_linage, \
    complete_chat, default_kwargs_chat_openai, \
    verbose, get_prompt_for_useful_notes, get_nearby_paths_in_prompt


class RetrievalWriter(Writer):
    def __init__(self, objective, caller_path: str):
        self.objective = objective
        super().__init__("auto", ["objective"], caller_path)

    def _write(self, note: Note) -> str:

        for comment in self._revise_comments[:-1]:
            if comment.type == "set":
                raise Exception("You can only use set for the last revise comment.")
        if len(self._revise_comments) > 0 and self._revise_comments[-1].type == "set":
            return self._revise_comments[-1].content

        nearby_notes = get_notes_by_linage(note)
        nearby_paths_in_prompt = get_nearby_paths_in_prompt(nearby_notes)

        revise_prompt = self.get_revise_prompt()
        object_prompt = f"""
You are writing for the following objective:
{self.objective}
"""
        header_prompt = revise_prompt + object_prompt

        prompt = header_prompt + f"""
There is a knowledge base to use. Here are some potentially useful paths of knowledge with their indices:
{nearby_paths_in_prompt}
Select some of the paths and output a list of indices ordered in the order you want to read them.
You should not include the indices that are irrelevant to the objective.
You should output in the format: index_1_to_read, index_2_to_read,... (e.g. 3,2,1)
"""
        chat = Chat(prompt)
        res = complete_chat(chat, default_kwargs_chat_openai)
        useful_indices = [int(item) for item in res.split(",")]
        useful_notes = [nearby_notes[i] for i in useful_indices]
        prompt = get_prompt_for_useful_notes(useful_notes)


class AutoWriter(Writer):
    def __init__(self, objective, caller_path: str):
        self.objective = objective
        super().__init__("auto", ["objective"], caller_path)

    def get_revise_prompt(self):
        if len(self._revise_comments) == 0:
            return ""
        revise_comment = []
        for comment in self._revise_comments:
            if comment.type == "revise":
                revise_comment.append("- "+comment.content)
        revise_prompt = f"""
        You are provided with the following notices:
        {revise_comment}"""

    def _write(self, note: Note) -> str:

        for comment in self._revise_comments[:-1]:
            if comment.type == "set":
                raise Exception("You can only use set for the last revise comment.")
        if len(self._revise_comments) > 0 and self._revise_comments[-1].type == "set":
            return self._revise_comments[-1].content

        nearby_notes = get_notes_by_linage(note)
        nearby_paths_in_prompt = get_nearby_paths_in_prompt(nearby_notes)

        revise_prompt = self.get_revise_prompt()
        object_prompt = f"""
You are writing for the following objective:
{self.objective}
"""
        header_prompt = revise_prompt+object_prompt

        prompt = header_prompt+f"""
There is a knowledge base to use. Here are some potentially useful paths of knowledge with their indices:
{nearby_paths_in_prompt}
Select some of the paths and output a list of indices ordered in the order you want to read them.
You should not include the indices that are irrelevant to the objective.
You should output in the format: index_1_to_read, index_2_to_read,... (e.g. 3,2,1)
"""
        chat = Chat(prompt)
        res = complete_chat(chat, default_kwargs_chat_openai)
        useful_indices = [int(item) for item in res.split(",")]
        useful_notes = [nearby_notes[i] for i in useful_indices]
        useful_prompt = get_prompt_for_useful_notes(useful_notes)
        if verbose:
            print("===Information Loaded===")
            print(useful_prompt)
        prompt = header_prompt+f"""
Here are some potentially useful notes:
{useful_prompt}
"""
        chat = Chat(prompt)
        res = complete_chat(chat, default_kwargs_chat_openai)
        return res


def auto(objective: str):
    """
    Auto generate code to achieve the objective
    :param objective:
    :return:
    """
    _, _, stack = EvolverInstance.get_context()
    return AutoWriter(objective, stack[0].filename)
