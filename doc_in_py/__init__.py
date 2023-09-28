from __future__ import annotations

from typing import Tuple, List


class Struct:
    def __init__(self, struct_type: str, obj: any, pos: Tuple[int, int] | None,
                 name: str = None):
        self.struct_type = struct_type
        self.obj = obj
        self.pos = pos
        self.children: List[Struct] = []
        self.name = name

    def __str__(self):
        return f"{self.struct_type}: {self.name}"
