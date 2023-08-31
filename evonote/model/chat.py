import copy

from evonote.model.llm import complete_chat, complete_chat_expensive


class Chat:
    """
    Class for storing the chat history for OpenAI API call
    """

    def __init__(self, user_message=None, system_message: any = None):
        self.history = []
        self.system_message = system_message
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
            res.append(f"{entry['role']}: {entry['content']}")
        return "\n".join(res)


    def complete_chat(self, options=None):
        complete_chat(self, options=options)

    def complete_chat_expensive(self, options=None):
        complete_chat_expensive(self, options=options)