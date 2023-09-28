from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from evonote.model.chat import Chat

normal_model = ""
expensive_model = ""

"""
## Chat completion
"""


def complete_chat(chat: Chat, options=None):
    raise NotImplementedError
    options = options or {}
    _options = {**options, "model": normal_model}
    return  # the res


def complete_chat_expensive(chat: Chat, options=None):
    raise NotImplementedError
    options = options or {}
    _options = {**options, "model": expensive_model}
    return  # the res
