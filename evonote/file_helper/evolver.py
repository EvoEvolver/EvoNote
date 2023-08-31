import ast
import inspect
import warnings

from evonote.file_helper.core import delete_old_comment_output
from evonote import EvolverInstance


def inline(func, **kwargs):
    manager, line_i, stacks = EvolverInstance.get_context()
    caller_id = get_caller_id(stacks[0])
    manager.clear_ops_for_caller(caller_id)
    code_line = manager.get_src_line(line_i)
    if check_if_stand_alone_call(code_line) is None:
        return
    source = inspect.getsource(func)
    source_lines = source.splitlines()[1:]
    source_indent = len(source_lines[0]) - len(source_lines[0].lstrip())
    inline_args = []
    for key, value in kwargs.items():
        inline_args.append(f"{key} = {repr(value)}")
    # remove indents of each line
    source_lines = inline_args + [line[source_indent:] for line in source_lines]
    new_source = "\n".join(source_lines)
    commented_line = "#" + code_line.lstrip()
    manager.insert_with_same_indent_after(caller_id, line_i,
                                          [new_source, "", commented_line])

    manager.del_origin_lines(caller_id, line_i, line_i)


def show(var):
    evolver_id = "show"
    manager, line_i, stacks = EvolverInstance.get_context()
    caller_id = get_caller_id(stacks[0])
    manager.clear_ops_for_caller(caller_id)
    code_line = manager.get_src_line(line_i)
    if check_if_stand_alone_call(code_line) is None:
        return
    delete_old_comment_output(manager, caller_id, line_i, evolver_id)
    lines_to_insert = str(var).splitlines()
    manager.insert_comment_with_same_indent_after(caller_id, line_i, lines_to_insert,
                                                  evolver_id)


def __warn_not_stand_alone_call(code_line):
    warnings.warn(f"'{code_line}' is not a stand-alone call. Ignored.", stacklevel=3)


def check_if_stand_alone_call(code_line):
    arg_names = []
    code_line = code_line.lstrip()
    try:
        tree = ast.parse(code_line)
        if len(tree.body) != 1:
            __warn_not_stand_alone_call(code_line)
            return
        expr = tree.body[0]
        if not isinstance(expr, ast.Expr):
            __warn_not_stand_alone_call(code_line)
            return
        value = expr.value
        if not isinstance(value, ast.Call):
            __warn_not_stand_alone_call(code_line)
            return
        for arg in value.args:
            if isinstance(arg, ast.Name):
                arg_names.append(arg.id)
            else:
                arg_names.append(None)
    except:
        __warn_not_stand_alone_call(code_line)
        return None
    return arg_names


def get_caller_id(stack):
    caller_id = stack.filename + ":" + str(stack.lineno)
    return caller_id


"""
def let(var):
    manager, line_i, stacks = EvolverInstance.get_context()
    code_line = manager.get_src_line(line_i)
    args = check_if_stand_alone_call(code_line)
    caller_id = get_caller_id(stacks[0])
    manager.clear_ops_for_caller(caller_id)
    if args is None:
        return
    assert len(args) == 1
    var_id = args[0]
    if var_id is None:
        warnings.warn("The argument of let() is not a direct variable. Ignored.")
        return
    arg_name = args[0]
    replacing_line = ""
    #if hasattr(var, "set") and var.override_assign:
    #    LHS_value += "set"
    if isinstance(var, ValueByInput):
        replacing_line += arg_name+".set("+var.self_value_in_code()+", \""+var.input_hash+"\")"
        manager.insert_with_same_indent_after(caller_id, line_i,
                                              [replacing_line])
    else:
        raise NotImplementedError()

    # Delete the let(...) line
    manager.del_origin_lines(caller_id, line_i, line_i)
    return

    stringified_var = None
    if isinstance(var, str):
        # stringified_var = get_stringified_string_with_indent(var, manager.get_indent(line_i))
        stringified_var = get_stringified_string()
    elif hasattr(var, "self_value_in_code"):
        stringified_var = var.self_value_in_code()
    else:
        raise NotImplementedError()

    manager.insert_with_same_indent_after(caller_id, line_i, [f'{LHS_value} = {stringified_var}'])


def retake(var: ValueByInput):
    manager, line_i, stacks = EvolverInstance.get_context()
    filepath = stacks[0].filename
    #caller_id = get_caller_id(stacks[0])
    #manager.del_origin_lines(caller_id, line_i, line_i)
    new_var = var.retake()
    EvolverInstance.add_value_to_cache(new_var, filepath)
    var.__dict__["value"] = new_var.value
"""


def evolve(output_path=None):
    _, _, stacks = EvolverInstance.get_context()
    if stacks[0].frame.f_locals["__name__"] != "__main__":
        # warnings.warn("update() is not called in __main__. Ignored.")
        return
    EvolverInstance.update_all_file()
    EvolverInstance.save_all_cache_to_file()
    EvolverInstance.save_all_output_to_file()


def save_cache():
    EvolverInstance.save_all_cache_to_file()


def discard_cache():
    EvolverInstance.discard_cache_update()


def save():
    EvolverInstance.save_all_cache_to_file()
    EvolverInstance.save_all_output_to_file()
