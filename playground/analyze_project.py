from evonote.notetree.analysis import analyze_notetree_sparsity
import evonote
from evonote.transform.module_to_notetree import get_notetree_for_module

notetree = get_notetree_for_module(evonote)
analyze_notetree_sparsity(notetree)