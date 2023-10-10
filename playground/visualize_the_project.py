import evonote
from evonote.transform.module_to_tree import get_tree_for_module

tree = get_tree_for_module(evonote)
tree.show_tree_gui()