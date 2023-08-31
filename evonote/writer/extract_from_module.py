from typing import Dict
from evonote.core.note import make_notebook_root, Note
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
        note_root, notebook = make_notebook_root("Notebook of module: " + self.root_module_name)
        build_notebook_for_module(self.tree, note_root, self.doc_parser)
        return notebook


def get_doc_in_prompt(doc_tuple):
    general, params, returns = doc_tuple
    if len(general)>0:
        doc = general + "\n"
    else:
        doc = ""
    for param_name, param_doc in params.items():
        doc += "Parameter " + param_name + ": " + param_doc + "\n"
    if len(returns)>0:
        doc += "Return value: " + returns + "\n"
    return doc

def build_notebook_for_module(leaf, root_note: Note, doc_parser):
    child_note = Note(root_note.default_notebook)
    root_note.add_child(leaf["type"]+": "+leaf["name"], child_note)
    child_note.type = "code:"+leaf["type"]
    child_note.related_info["object"] = leaf["obj"]
    doc = inspect.getdoc(leaf["obj"])
    if doc is not None:
        child_note.be(doc)
    for name, child in leaf["children"].items():
        if child["type"] == "function":
            doc = inspect.getdoc(child["obj"])
            if doc is None:
                doc = " ".join(name.split("_"))
            doc_tuple = doc_parser(doc)
            function_note = child_note.s("function: "+name)
            function_note.be(get_doc_in_prompt(doc_tuple))
            function_note.type = "code:function"
            if len(doc_tuple[0])>0:
                child_note.related_info["annotation"] = doc_tuple[0]
            if len(doc_tuple[1])>0:
                child_note.related_info["parameter annotation"] = doc_tuple[1]
            if len(doc_tuple[2])>0:
                child_note.related_info["return value annotation"] = doc_tuple[2]
        elif child["type"] == "module":
            build_notebook_for_module(child, child_note, doc_parser)
        elif child["type"] == "class":
            build_notebook_for_module(child, child_note, doc_parser)


def parse_pycharm_doc(doc: str):
    """
    Parse the docstring generated by PyCharm
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

        content = line[content_start:]
        if state == "param":
            params[param_name] = params.get(param_name, "") + content.strip()
        elif state == "return":
            returns += content.strip()
        else:
            general += content.strip()
    return general, params, returns


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
            params[param_name] = params.get(param_name, "") +" "+ new_content.strip()
        elif state == "return":
            returns += content.strip()
        else:
            general += content.strip()
    return general, params, returns



def get_class_members(cls, tree_root: Dict):
    for name, member in inspect.getmembers(cls, predicate=inspect.isfunction):
        tree_root[name] = {"type": "function", "obj": member}

def get_module_members(module, manager: ModuleManager, tree_root: Dict, root_path: str):
    for name, member in inspect.getmembers(module):
        # check the type of the member is in module, class, method, function
        if str(type(member)) not in ["<class 'module'>", "<class 'type'>",
                                     "<class 'function'>"]:
            continue
        # skip the members defined outside the root path
        try:
            member_path = inspect.getfile(member)
        except:
            continue
        if not member_path.startswith(root_path):
            continue
        key = (member_path, name)
        if inspect.ismodule(member):
            if key in manager.modules:
                continue
            manager.modules[key] = member
            new_tree_root = {}
            tree_root[name] = {"type": "module", "children": new_tree_root, "obj": member, "name": name}
            get_module_members(member, manager, new_tree_root, member_path)
        elif inspect.isclass(member):
            manager.classes[key] = member
            tree_root[name] = {"type": "class", "obj": member, "name": name, "children": {}}
            get_class_members(member, tree_root[name]["children"])
        elif inspect.isfunction(member):
            manager.functions[key] = member
            tree_root[name] = {"type": "function", "obj": member, "name": name}
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