import importlib
import os
import pkgutil
from typing import Dict, List, Callable, Tuple
from evonote.core.note import Note
from evonote.core.notebook import make_notebook_root
import inspect


class ModuleManager:
    def __init__(self, module, doc_parser=None):
        self.root_module = module
        self.root_path = module.__file__.split("__init__.py")[0]
        self.root_module_name = module.__name__
        self.functions = {}
        self.classes = {}
        self.modules = {}
        self.doc_parser = doc_parser if doc_parser is not None else parse_pycharm_doc
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
        build_notebook_for_module(self.tree, note_root, self.doc_parser)
        return notebook


def get_doc_in_prompt(doc_tuple):
    general, params, returns = doc_tuple
    if len(general) > 0:
        doc = general + "\n"
    else:
        doc = ""
    for param_name, param_doc in params.items():
        doc += "Parameter " + param_name + ": " + param_doc + "\n"
    if len(returns) > 0:
        doc += "Return value: " + returns + "\n"
    return doc


class FunctionDocs:
    def __init__(self, general: str, params: Dict[str, str], returns: str,
                 keywords: List[str]):
        self.general: str = general if general is not None else ""
        self.params: Dict[str, str] = params if params is not None else {}
        self.returns: str = returns if returns is not None else ""
        self.keywords: List[str] = keywords if keywords is not None else []


Doc_parser_res = Tuple[str, Dict[str, str], str, List[str]]

Doc_parser = Callable[[str], Doc_parser_res]


def build_notebook_for_module(leaf, root_note: Note, doc_parser: Doc_parser):
    child_note = Note(root_note.default_notebook)
    child_key = leaf["type"] + ": " + leaf["name"]
    root_note.add_child(child_key, child_note)
    child_type = "code:" + leaf["type"]
    child_obj = leaf["obj"]
    docs = inspect.getdoc(leaf["obj"])
    child_note.resource.add_resource(child_obj, child_type, docs)

    for name, child in leaf["children"].items():
        docs = {}
        if child["type"] == "function":
            doc_raw = inspect.getdoc(child["obj"])
            if doc_raw is None:
                docs = " ".join(name.split("_"))
                general, parameter, return_value, keywords = ("", {}, "", [])
            else:
                general, parameter, return_value, keywords = doc_parser(doc_raw)
            function_note = child_note.s("function: " + name)
            function_note.be(name)
            function_docs = FunctionDocs(general, parameter, return_value, keywords)
            function_note.resource.add_function(child["obj"], function_docs)
        elif child["type"] == "module":
            build_notebook_for_module(child, child_note, doc_parser)
        elif child["type"] == "class":
            build_notebook_for_module(child, child_note, doc_parser)


def parse_pycharm_doc(doc: str) -> Doc_parser_res:
    """
    Parse the docstring generated by PyCharm
    :param doc: raw docstring
    :return: general, params, returns, keywords
    :keyword: parsing, docstring
    """
    state = "general"
    general = ""
    params = {}
    param_name = ""
    returns = ""
    keywords = []
    doc_lines = doc.split("\n")
    for line in doc_lines:
        content_start = 0
        if line.startswith(":param"):
            # find next :
            next_colon = line.find(":", 6)
            if next_colon != -1:
                param_name = line[6:next_colon].strip()
                state = "param"
                content_start = next_colon + 1
        elif line.startswith(":return:"):
            state = "return"
            content_start = 8
        elif line.startswith(":keyword:"):
            state = "keyword"
            content_start = 9

        content = line[content_start:]
        if state == "param":
            params[param_name] = params.get(param_name, "") + content.strip()
        elif state == "return":
            returns += content.strip()
        elif state == "keyword":
            keywords.extend(content.strip().split(","))
        else:
            general += content.strip()
    return general, params, returns, keywords


def parse_vscode_doc(doc: str):
    """
    Parse the docstring generated by VSCode
    :param doc:
    :return:
    """
    state = "general"
    general = ""
    params = {}
    param_name = ""
    returns = ""
    doc_lines = doc.split("\n")
    for line in doc_lines:
        content_start = 0
        if line.startswith("Args:"):
            state = "param"
            content_start = 5
            continue
        elif line.startswith("Returns:"):
            state = "return"
            content_start = 8

        content = line[content_start:]
        if state == "param":
            # find next :
            next_colon = line.find(":")
            new_content = line
            if next_colon != -1:
                param_name = line[:next_colon].strip()
                state = "param"
                content_start = next_colon + 1
                new_content = line[content_start:]
            params[param_name] = params.get(param_name, "") + " " + new_content.strip()
        elif state == "return":
            returns += content.strip()
        else:
            general += content.strip()
    return general, params, returns


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


def get_module_members(module, manager: ModuleManager, tree_root: Dict, root_path: str):
    module_dir = os.path.dirname(inspect.getfile(module))
    sub_modules = []
    is_pkg = hasattr(module, "__path__")
    if is_pkg:
        for sub_module_info in pkgutil.iter_modules([module_dir]):
            sub_module = importlib.import_module(
                module.__name__ + "." + sub_module_info.name)
            sub_modules.append(sub_module)

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
        key = (member_path, name)
        if inspect.isclass(member):
            manager.classes[key] = member
            tree_root[name] = {"type": "class", "obj": member, "name": name,
                               "children": {}}
            get_class_members(member, tree_root[name]["children"])
        elif inspect.isfunction(member):
            manager.functions[key] = member
            tree_root[name] = {"type": "function", "obj": member, "name": name}

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


def get_notebook_for_module(module, doc_parser_type="pycharm"):
    if doc_parser_type == "pycharm":
        doc_parser = parse_pycharm_doc
    elif doc_parser_type == "vscode":
        doc_parser = parse_vscode_doc
    else:
        raise ValueError("doc_parser_type should be pycharm or vscode")
    manager = ModuleManager(module, doc_parser)
    notebook = manager.build_notebook()
    return notebook


if __name__ == "__main__":
    from evonote.testing import v_lab

    manager = ModuleManager(v_lab)
    notebook = manager.build_notebook()
    notebook.show_notebook_gui()
