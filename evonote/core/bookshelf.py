from typing import List

from evonote.core.note import Notebook


class Bookshelf:

    def __init__(self):
        self.notebooks: List[Notebook] = []