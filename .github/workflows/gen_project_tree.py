import evonote, json
from evonote.gui.mindtree import get_json_for_treemap
from evonote.transform.module_to_tree import get_tree_for_module
tree = get_tree_for_module(evonote)
tree_in_dict = get_json_for_treemap(tree.root)
f = open('output/project_tree.json', 'w');json.dump(tree, f)