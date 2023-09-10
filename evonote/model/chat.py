from __future__ import annotations
import copy
import inspect

from evonote.gui.dictionary_viewer import show_document_with_key_gui
from evonote.model.openai import complete_chat, complete_chat_expensive

chat_loggers = []

class ChatLogger:
    def __init__(self):
        self.chat_list = []
        # the path of the file that calls this function
        self.caller_list = []

    def __enter__(self):
        chat_loggers.append(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        chat_loggers.remove(self)
        contents = [str(chat) for chat in self.chat_list]
        filenames = [caller_name.split("/")[-1] for caller_name in self.caller_list]
        show_document_with_key_gui(filenames, contents)



class Chat:
    """
    Class for storing the chat history for OpenAI API call
    """

    def __init__(self, user_message=None, system_message: any = None):
        self.history = []
        self.system_message = system_message
        if user_message is not None:
            self.add_message(user_message, "user")

    def add_message(self, content: any, role: str):
        self.history.append({
            "content": content,
            "role": role
        })

    def ask(self, content: any):
        self.add_user_message(content)

    def add_user_message(self, content: any):
        self.add_message(content, "user")

    def add_assistant_message(self, content: any):
        self.add_message(content, "assistant")

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

    def __str__(self):
        res = []
        log_list = self.get_log_list()
        for entry in log_list:
            res.append(f"------{entry['role']}------\n {entry['content']}")
        return "\n".join(res)

    def complete_chat(self, options=None):
        res = complete_chat(self, options=options)
        self.add_assistant_message(res)
        if len(chat_loggers) > 0:
            # get the file that calls this function
            caller_name = inspect.stack()[1].filename
            for chat_logger in chat_loggers:
                chat_logger.chat_list.append(self)
                chat_logger.caller_list.append(caller_name)
        return res

    def complete_chat_expensive(self, options=None):
        res = complete_chat_expensive(self, options=options)
        self.add_assistant_message(res)
        if len(chat_loggers) > 0:
            # get the file that calls this function
            caller_name = inspect.stack()[1].filename
            for chat_logger in chat_loggers:
                chat_logger.chat_list.append(self)
                chat_logger.caller_list.append(caller_name)
        return res
