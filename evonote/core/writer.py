from __future__ import annotations

import json

import typing

from evonote import EvolverInstance

from evonote.file_helper.evolver import get_caller_id


verbose = True

if typing.TYPE_CHECKING:
    from evonote.core.note import Note


class Writer:
    def __init__(self, writer_type: str | None, key_for_hash,
                 caller_path: str | None = None):
        self._writer_type: str | None = writer_type
        self._caller_path: str | None = caller_path
        self._key_for_hash = key_for_hash

        self._need_retake = False
        self._revise_comments: typing.List[ReviseLog] = []

        self._is_writer = True

        self._after_assign: typing.List[typing.Callable[[Note], None]] = []

    def _get_comp_result(self, note: Note):
        """
        Compute something that is computationally expensive and return the result
        Will use cache if possible
        :param note:
        :return:
        """
        input_for_hash = {
            key: self.__dict__[key] for key in self._key_for_hash
        }
        
        input_for_hash = (input_for_hash, note.note_path, [str(item) for item in self._revise_comments])

        cache = EvolverInstance.read_cache(input_for_hash,
                                           self._writer_type,
                                           self._caller_path, True)

        if cache.is_valid() and not self._need_retake:
            return cache._value
        result = self._write(note)
        if verbose:
            print("=======Input=======")
            print(input_for_hash)
            print("======Result======")
            print(result)
        cache.set_cache(result)
        return result

    def _set_with_comp_result(self, comp_result, note: Note):
        note.be(comp_result)

    def _write(self, note: Note):
        raise NotImplementedError()

    def retake(self):
        self._need_retake = True
        return self

    def revise(self, comment: str):
        self._revise_comments.append(ReviseLog("revise", comment))
        return self

    def set(self, content):
        self._revise_comments.append(ReviseLog("set", content))
        return self

    def to_here(self):
        self._after_assign.append(_to_here)
        return self

class ReviseLog:
    def __init__(self, type, content, options=None):
        self.type = type
        self.content = content
        self.options = options

    def __str__(self):
        return json.dumps({
            "type": self.type,
            "content": self.content,
            "options": self.options
        })

def _to_here(note: Note, manager, line_i, stacks):
    #manager, line_i, stacks = EvolverInstance.get_context()
    code_line = manager.get_src_line(line_i)
    while "to_here()" not in code_line:
        line_i += 1
        code_line = manager.get_src_line(line_i)
    code_line: str
    caller_id = get_caller_id(stacks[0])
    manager.clear_ops_for_caller(caller_id)

    new_line = code_line.lstrip().replace("to_here()", 'set("""' + str(note) + '""")')

    manager.insert_with_same_indent_after(caller_id, line_i,
                                          [new_line])

    manager.del_origin_lines(caller_id, line_i, line_i)


default_kwargs_chat_openai = {"model": "gpt-3.5-turbo"}


class ChatWriter(Writer):
    def __init__(self, user_message, system_message, caller_path: str):
        self.user_message = user_message
        self.system_message = system_message
        super().__init__("chat", ["user_message", "system_message"], caller_path)

    def _write(self, note: Note) -> str:
        chat = Chat(user_message=self.user_message, system_message=self.system_message)
        result = None

        for comment in self._revise_comments:
            if comment.type == "set":
                result = comment.content
            elif comment.type == "revise":
                if result is None:
                    result = chat.complete_chat()
                chat.add_assistant_message(result)
                chat.add_user_message(comment.content)
                result = None

        if result is None:
            result = chat.complete_chat()

        return result


def get_notes_by_linage(note: Note, depth=2):
    linage = [note]
    for _ in range(depth):
        linage.append(linage[-1].parents)
    nearby_notes = []
    for item in linage:
        for key, child in item.children.items():
            nearby_notes.append(child)
    return nearby_notes


from evonote.model.chat import Chat


def answer_simple(question: str):
    return answer(question, system_message="Answer everything succinctly")

def answer_list(question: str):
    return answer(question, system_message='Answer EVERYTHING with a JSON list such as ["1","2","3"]')


def answer(question: str, system_message: str = None, format=None) -> ChatWriter | str:
    """
    One turn ask and answer
    :param question:
    :param system_message:
    :param kwargs:
    :return:
    """
    _, _, stack = EvolverInstance.get_context()
    return ChatWriter(question, system_message, stack[0].filename)


def get_prompt_for_useful_notes(notes: typing.List[Note]):
    prompt = []
    for i, note in enumerate(notes):
        if note.content == "" and len(note.children) == 0:
            continue
        line = [note.note_path + ":"]
        line.append(note.content)
        prompt.append(" ".join(line))
    return "\n".join(prompt)


def get_nearby_paths_in_prompt(notes: typing.List[Note], n_preview_words=10):
    lines = []
    for i, note in enumerate(notes):
        if note.content == "" and len(note.children) == 0:
            continue
        line = [str(i)+"."]
        line.append(note.note_path)
        raw_content = note.content
        if len(raw_content) > 0:
            words = raw_content.split(" ")
            preview = " ".join(words[:n_preview_words])
            line.append(": "+preview.strip())
        else:
            if len(note.children) > 0:
                line.append(": (has children)")
        lines.append(" ".join(line))
    return "\n".join(lines)
