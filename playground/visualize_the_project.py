import evonote
from evonote.transform.module_to_notetree import get_notetree_for_module

notetree = get_notetree_for_module(evonote)
notetree.show_notetree_gui()