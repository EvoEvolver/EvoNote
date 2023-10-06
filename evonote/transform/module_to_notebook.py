from __future__ import annotations

import inspect
import json

from doc_in_py.core import get_module_members
from doc_in_py import Struct
from evonote.notebook.note import Note
from evonote.notebook.notebook import Notebook
from doc_in_py.docs_parser import \
    parse_rst_docstring, \
    parse_google_docstring, Doc_parser

"""
This modules is for extract the information from python modules and build a notebook for it.


## Get notebook for module

"""


def get_notebook_for_module(module, docs_parser_type="rst"):
    if docs_parser_type == "rst":
        docs_parser = parse_rst_docstring
    elif docs_parser_type == "google":
        docs_parser = parse_google_docstring
    else:
        raise ValueError("docs_parser_type should be pycharm or vscode")
    module_name = module.__name__
    notebook = Notebook(
        "Notebook of module: " + module_name)
    module_struct = get_module_members(module)
    build_notebook_for_struct(module_struct, notebook.root, docs_parser)
    return notebook


def build_notebook_for_struct(curr_struct: Struct, root_note: Note,
                              docs_parser: Doc_parser):
    """
    :param curr_struct: The struct to be added to the child of the root_note
    :param root_note: The root note to be filled with children from curr_struct
    :param docs_parser: The parser for the docstring
    """
    curr_key = curr_struct.struct_type + ": " + curr_struct.name
    curr_note = root_note.new_child(curr_key)

    curr_type = "code:" + curr_struct.struct_type
    curr_obj = curr_struct.obj
    docs = inspect.getdoc(curr_struct.obj)
    curr_note.resource.add_resource(curr_obj, curr_type, docs)

    for child_struct in curr_struct.children:
        match child_struct.struct_type:
            case "function":
                process_function_struct(child_struct, curr_note, docs_parser)
            case "module":
                build_notebook_for_struct(child_struct, curr_note, docs_parser)
            case "class":
                build_notebook_for_struct(child_struct, curr_note, docs_parser)
            case "comment":
                curr_note.be(curr_note.content + "\n" + child_struct.obj)
            case "section":
                build_notebook_for_struct(child_struct, curr_note, docs_parser)
            case "todo":
                build_notebook_for_struct(child_struct, curr_note, docs_parser)
            case "example":
                build_notebook_for_struct(child_struct, curr_note, docs_parser)



def process_function_struct(function_struct: Struct, parent_node: Note, docs_parser):
    doc_raw = inspect.getdoc(function_struct.obj)
    if doc_raw is None:
        general, parameters, return_value = ("", {}, "")
    else:
        general, parameters, return_value = docs_parser(doc_raw)
    # Check if the function is callable
    if callable(function_struct.obj):
        parameters = {**get_empty_param_dict(function_struct.obj), **parameters}
    else:
        parameters = {**get_empty_param_dict(function_struct.obj.__func__), **parameters}
    if "self" in parameters:
        del parameters["self"]
    function_name = function_struct.name
    if not function_name.startswith("__example"):
        function_note = parent_node.s("function: " + function_name)
        function_note.be(general)
        function_note.resource.add_function(function_struct.obj, "function")
        if len(parameters) > 0:
            function_note.s("parameters").be(json.dumps(parameters))
        if len(return_value) > 0:
            function_note.s("return value").be(return_value)
    # this is a function demonstrate the usage the module
    else:
        function_note = parent_node.s("example: " + function_name)
        function_code = inspect.getsource(function_struct.obj)
        # replace first __example with example
        function_code = function_code.replace("__example", "example", 1)
        function_note.be(f"{function_code}")

def get_empty_param_dict(func):
    param_dict = {}
    for param_name in inspect.signature(func).parameters.keys():
        param_dict[param_name] = ""
    return param_dict

def get_docs_in_prompt(doc_tuple):
    general, params, returns = doc_tuple
    if len(general) > 0:
        docs = general + "\n"
    else:
        docs = ""
    for param_name, param_doc in params.items():
        docs += "Parameter " + param_name + ": " + param_doc + "\n"
    if len(returns) > 0:
        docs += "Return value: " + returns + "\n"
    return docs


if __name__ == "__main__":
    from evonote.testing.testing_modules import v_lab

    notebook = get_notebook_for_module(v_lab)
    notebook.show_notebook_gui()
