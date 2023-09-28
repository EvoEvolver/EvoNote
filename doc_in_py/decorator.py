"""
This file contains decorators for adding semantic information to functions.
The based design is to add attributes to the __dict__ of the function.
All the attributes are prefixed with "__docinpy_"
"""

"""
## Todo decorator
"""

default_todo_info = "This part is unfinished"


def todo(todo_info_or_func: str):
    """
    A decorator for marking the function or class as todo
    It sets the attribute __docinpy_todo in the __dict__ of the function or class
    """
    if isinstance(todo_info_or_func, str):
        return lambda func_or_class: _todo_decorator(func_or_class,
                                                     todo_info_or_func)
    else:
        return _todo_decorator(todo_info_or_func, default_todo_info)


def _todo_decorator(func_or_class, todo_info):
    if isinstance(func_or_class, type):
        func_or_class.__docinpy_todo = todo_info
    else:
        func_or_class.__dict__["__docinpy_todo"] = todo_info
    return func_or_class


"""
## Example decorator
"""


def example(func_or_class):
    func_or_class.__dict__["__docinpy_example"] = True
    return func_or_class
