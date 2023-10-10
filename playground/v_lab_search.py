from evonote.transform.module_to_tree import get_tree_for_module
from evonote.debug import display_chats, display_embedding_search
from evonote.search.code_searcher import search_function
from evonote.testing.testing_modules import v_lab

tree = get_tree_for_module(v_lab)

with display_embedding_search():
    with display_chats():
        tree = search_function("Add water", tree)
        tree.show_tree_gui()
