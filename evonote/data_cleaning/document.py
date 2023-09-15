from __future__ import annotations
from typing import List


class Document:
    def __init__(self, title="", content="", sections=None):
        self.title = title
        self.content = content
        self.sections: List[Document] = sections if sections is not None else []

    def iter_sections(self, root_path="") -> (Document, str):
        # TODO this is not tested
        if len(self.content) > 0:
            yield self, root_path + "\\" + self.title
        for section in self.sections:
            yield from section.iter_sections(root_path=root_path + "\\" + self.title)