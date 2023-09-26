from __future__ import annotations
from typing import Tuple, TypedDict

# module_struct = [struct_type, obj, (start_pos, end_pos)]

module_struct = Tuple[str, any, Tuple[int, int]]

class ModuleTreeNode(TypedDict):
    type: str
    obj: any
    name: str
    children: dict[str, ModuleTreeNode]