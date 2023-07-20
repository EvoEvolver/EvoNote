import ast

from evonote import EvolverInstance
from evonote.data_type.var_types import ValueByInput
from evonote.io.utils import get_abs_path

class Stream:
    def __init__(self, contents: list):
        self.contents = contents
        self.index = 0

    def read_next(self) -> str:
        if self.index >= len(self.contents):
            return None
        else:
            self.index += 1
            return self.contents[self.index - 1]

    def read_back(self) -> str:
        if self.index <= 0:
            return None
        else:
            self.index -= 1
            return self.contents[self.index]

    def go_to_beginning(self):
        self.index = 0

def read(file_path) -> Stream:
    """
    :param file_path: The path to the file to read.
    :return: A stream of paragraphs by splitting the file by two newlines.
    """
    caller_path = EvolverInstance.get_context()[2][0].filename
    abs_path = get_abs_path(file_path, caller_path)
    src = open(abs_path, "r").read()
    paragraphs = src.split("\n\n")
    return Stream(paragraphs)

import json
_supported_langs = ["JSON"]
def parse(src: ValueByInput | str, lang: str="JSON"):
    """
    :param src: The source code to parse.
    :param lang: The language of the source code.
    """
    _src = str(src)
    if lang not in _supported_langs:
        raise Exception("Unsupported language: " + lang)
    try:
        if lang == "JSON":
            # Ignore the period at the end of the source
            if _src[-1] == ".":
                _src = _src[:-1]
            parsed_dict = ast.literal_eval(_src)
            if isinstance(src, ValueByInput):
                return ValueByInput(parsed_dict, src.input_hash, src.input, src.type)
            else:
                return parsed_dict
    except Exception as e:
        print("Parse failed on:\n" + str(_src))
        print("Error: " + str(e))
        return None

