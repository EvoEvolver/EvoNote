import ast


def robust_json_parse(src: str):
    # find first {
    start = src.find("{")
    # find last }
    end = src.rfind("}")
    if start == -1 or end == -1:
        raise ValueError(f"Invalid json: {src}")
    try:
        res = ast.literal_eval(src[start:end + 1])
    except:
        raise ValueError(f"Invalid json: {src}")
    return res


import sys

def debugger_is_active() -> bool:
    """Return if the debugger is currently active"""
    return hasattr(sys, 'gettrace') and sys.gettrace() is not None