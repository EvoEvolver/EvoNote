import os


def get_abs_path(out_path, caller_path):
    if os.path.isabs(out_path):
        abs_path = out_path
    else:
        abs_path = os.path.join(os.path.dirname(caller_path), out_path)
    abs_path = os.path.normpath(abs_path)
    return abs_path
