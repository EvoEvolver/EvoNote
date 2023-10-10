from docinpy import Struct


def to_dict(struct: Struct):
    dict = {
        "struct_type": struct.struct_type,
    }
    if struct.name is not None:
        dict["name"] = struct.name
    # check if the obj is a string
    if isinstance(struct.obj, str):
        dict["obj"] = struct.obj
    if len(struct.children) > 0:
        dict["children"] = [to_dict(c) for c in struct.children]
    return dict
