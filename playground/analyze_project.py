from evonote.mindtree.analysis import analyze_tree_sparsity
import evonote
from evonote.transform.module_to_tree import get_tree_for_module

tree = get_tree_for_module(evonote)
analyze_tree_sparsity(tree)