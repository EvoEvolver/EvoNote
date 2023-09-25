from __future__ import annotations

import copy

from evonote.file_helper.logger import Logger
from evonote.gui.dictionary_viewer import show_document_with_key_gui
from evonote.model.openai import (complete_chat as openai_complete_chat,
                                  complete_chat_expensive as openai_complete_chat_expensive,
                                  model_list as openai_model_list)
from evonote.model.openllm import (complete_chat as openllm_complete_chat,
                                   complete_chat_expensive as openllm_complete_chat_expensive)


class ChatLogger(Logger):
    active_loggers = []

    def display_log(self):
        contents = [str(chat) for chat in self.log_list]
        filenames = [caller_name.split("/")[-1] for caller_name in self.caller_list]
        show_document_with_key_gui(filenames, contents)


class Chat:
    """
    Class for chat completion
    """

    def __init__(self, user_message=None, system_message: any = None):
        self.history = []
        self.system_message = system_message
        if user_message is not None:
            self._add_message(user_message, "user")

    def _add_message(self, content: any, role: str):
        self.history.append({
            "content": content,
            "role": role
        })

    def ask(self, content: any):
        self.add_user_message(content)

    def add_user_message(self, content: any):
        self._add_message(content, "user")

    def add_assistant_message(self, content: any):
        self._add_message(content, "assistant")

    def __copy__(self):
        new_chat_log = Chat(system_message=self.system_message)
        new_chat_log.history = copy.deepcopy(self.history)
        return new_chat_log

    def get_log_list(self):
        """
        :return: chat log for sending to the OpenAI API
        """
        res = []
        if self.system_message is not None:
            res.append({
                "content": str(self.system_message),
                "role": "system"
            })
        for message in self.history:
            res.append({
                "content": str(message["content"]),
                "role": message["role"]
            })
        return res

    def complete_chat(self, options=None):
        options = options or {}
        if use_openai_model(options):
            res = openai_complete_chat(self, options=options)
        else:
            res = openllm_complete_chat(self, options=options)
        self.add_assistant_message(res)
        if len(ChatLogger.active_loggers) > 0:
            for chat_logger in ChatLogger.active_loggers:
                chat_logger.add_log(self)
        return res

    def complete_chat_expensive(self, options=None):
        options = options or {}
        if use_openai_model(options):
            res = openai_complete_chat_expensive(self, options=options)
        else:
            res = openllm_complete_chat_expensive(self, options=options)
        self.add_assistant_message(res)
        if len(ChatLogger.active_loggers) > 0:
            for chat_logger in ChatLogger.active_loggers:
                chat_logger.add_log(self)
        return res

    def __str__(self):
        res = []
        log_list = self.get_log_list()
        for entry in log_list:
            res.append(f"------{entry['role']}------\n {entry['content']}")
        return "\n".join(res)


def use_openai_model(options) -> bool:
    return options.get("model", "gpt-3.5-turbo") in openai_model_list
