import importlib
import inspect
import os
import pkgutil
from typing import Dict, Tuple

from evonote.notebook.note import Note
from evonote.notebook.notebook import make_notebook_root
from evonote.transform.module_to_notebook.docs_parser import parse_reStructuredText_docs, \
    parse_google_docs, FunctionDocs, Doc_parser, get_in_module_structs


class ModuleManager:
    def __init__(self, module, docs_parser=None):
        self.root_module = module
        self.root_path = module.__file__.split("__init__.py")[0]
        self.root_module_name = module.__name__
        self.functions = {}
        self.classes = {}
        self.modules = {}
        self.docs_parser = docs_parser if docs_parser is not None else parse_reStructuredText_docs
        self.tree: Dict = {}

        self.get_module_members()

    def get_module_members(self):
        new_tree_root = {}
        tree = {"type": "module", "obj": self.root_module, "children": new_tree_root,
                "name": self.root_module_name}
        get_module_members(self.root_module, self, new_tree_root, self.root_path)
        self.tree = tree
        return self

    def build_notebook(self):
        note_root, notebook = make_notebook_root(
            "Notebook of module: " + self.root_module_name)
        build_notebook_for_module(self.tree, note_root, self.docs_parser)
        return notebook


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


def build_notebook_for_module(leaf, root_note: Note, docs_parser: Doc_parser):
    child_note = Note(root_note.default_notebook)
    child_key = leaf["type"] + ": " + leaf["name"]
    root_note.add_child(child_key, child_note)
    child_type = "code:" + leaf["type"]
    child_obj = leaf["obj"]
    docs = inspect.getdoc(leaf["obj"])
    child_note.resource.add_resource(child_obj, child_type, docs)

    for name, child in leaf["children"].items():
        docs = {}
        match child["type"]:
            case "function":
                doc_raw = inspect.getdoc(child["obj"])
                if doc_raw is None:
                    docs = " ".join(name.split("_"))
                    general, parameter, return_value, keywords = ("", {}, "", [])
                else:
                    general, parameter, return_value, keywords = docs_parser(doc_raw)
                function_note = child_note.s("function: " + name)
                function_note.be(name)
                function_docs = FunctionDocs(general, parameter, return_value, keywords)
                function_note.resource.add_function(child["obj"], function_docs)
            case "module":
                build_notebook_for_module(child, child_note, docs_parser)
            case "class":
                build_notebook_for_module(child, child_note, docs_parser)
            case "comment":
                child_note.new_child(name).be(child["obj"])


def get_class_members(cls, tree_root: Dict):
    for name, member in inspect.getmembers(cls):
        if isinstance(member, classmethod):
            continue
        type_str = str(type(member))
        # check whether member is a function
        if type_str == "<class 'function'>":
            tree_root[name] = {"type": "function", "obj": member}
        # Add classmethods
        elif type_str == "<class 'mappingproxy'>":
            for sub_name, sub_member in member.items():
                if isinstance(sub_member, classmethod):
                    tree_root[sub_name] = {"type": "function", "obj": sub_member}


# module_struct = [struct_type, obj, (start_pos, end_pos)]

module_struct = Tuple[str, any, Tuple[int, int]]


def get_module_members(module, manager: ModuleManager, tree_root: Dict, root_path: str):
    module_dir = os.path.dirname(inspect.getfile(module))
    sub_modules = []
    is_pkg = hasattr(module, "__path__")
    if is_pkg:
        for sub_module_info in pkgutil.iter_modules([module_dir]):
            sub_module = importlib.import_module(
                module.__name__ + "." + sub_module_info.name)
            sub_modules.append(sub_module)

    functions = []
    classes = []

    for name in dir(module):
        member = module.__dict__[name]
        # check the type of the member is in module, class, method, function
        if (str(type(member)) not in ["<class 'type'>",
                                      "<class 'function'>"]):
            continue
        # skip the members defined outside the root path
        try:
            member_path = inspect.getfile(member)
        except:
            continue
        if not member_path.startswith(root_path):
            continue

        if inspect.isclass(member):
            classes.append(member)
        elif inspect.isfunction(member):
            functions.append(member)

    module_path = inspect.getfile(module)
    structs = get_in_module_structs(module, functions, classes)
    comment_index = 0
    for struct_type, struct, _ in structs:
        if struct_type == "comment":
            name = "comment_" + str(comment_index)
            tree_root[name] = {"type": "comment", "obj": struct, "name": name}
            comment_index += 1
            continue
        name = struct.__name__
        key = (module_path, name)
        match struct_type:
            case "function":
                manager.functions[key] = struct
                tree_root[name] = {"type": "function", "obj": struct, "name": name}
            case "class":
                manager.classes[key] = struct
                tree_root[name] = {"type": "class", "obj": struct, "name": name,
                                   "children": {}}
                get_class_members(struct, tree_root[name]["children"])


    for i, sub_module in enumerate(sub_modules):
        name = sub_module.__name__.split(".")[-1]
        member = sub_module
        member_path = inspect.getfile(member)
        key = (member_path, name)
        if key in manager.modules:
            continue
        manager.modules[key] = member
        new_tree_root = {}
        tree_root[name] = {"type": "module", "children": new_tree_root, "obj": member,
                           "name": name}
        get_module_members(member, manager, new_tree_root, member_path)

    return


def get_notebook_for_module(module, docs_parser_type="reStruct"):
    if docs_parser_type == "reStruct":
        docs_parser = parse_reStructuredText_docs
    elif docs_parser_type == "google":
        docs_parser = parse_google_docs
    else:
        raise ValueError("docs_parser_type should be pycharm or vscode")
    manager = ModuleManager(module, docs_parser)
    notebook = manager.build_notebook()
    return notebook


if __name__ == "__main__":
    from evonote.testing import v_lab

    manager = ModuleManager(v_lab)
    notebook = manager.build_notebook()
    notebook.show_notebook_gui()
