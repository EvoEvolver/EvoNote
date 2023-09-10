from __future__ import annotations
import inspect
from typing import List


class Logger:
    active_loggers: List[Logger] = []

    def __init__(self, file_path_scope: str | List[str] | None = None):
        self.log_list = []
        # the path of the file that calls this function
        self.caller_list = []
        self.file_path_scope = set()
        if file_path_scope is not None:
            if isinstance(file_path_scope, str):
                self.file_path_scope.add(file_path_scope)
            else:
                self.file_path_scope.update(file_path_scope)
            self.no_file_filter = False
        else:
            self.no_file_filter = True
        self.__class__.active_loggers = []

    def add_log(self, log: any):
        caller_path = inspect.stack()[2].filename
        if self.no_file_filter or caller_path in self.file_path_scope:
            self.caller_list.append(caller_path)
            self.log_list.append(log)

    @classmethod
    def add_log_to_all(cls, log: any):
        for logger in cls.active_loggers:
            logger.add_log(log)

    def __enter__(self):
        # Add self to active_loggers
        self.__class__.active_loggers.append(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__class__.active_loggers.remove(self)
        self.display_log()

    def display_log(self):
        raise NotImplementedError
