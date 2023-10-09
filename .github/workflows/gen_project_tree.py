import evonote, json
from evonote.gui.notetree import get_json_for_treemap
from evonote.transform.module_to_notetree import get_notetree_for_module
notetree = get_notetree_for_module(evonote)
tree = get_json_for_treemap(notetree.root)
f = open('output/project_tree.json', 'w');json.dump(tree, f)