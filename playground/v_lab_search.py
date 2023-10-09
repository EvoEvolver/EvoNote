from evonote.transform.module_to_notetree import get_notetree_for_module
from evonote.debug import display_chats, display_embedding_search
from evonote.search.code_searcher import search_function
from evonote.testing.testing_modules import v_lab

notetree = get_notetree_for_module(v_lab)

with display_embedding_search():
    with display_chats():
        notetree = search_function("Add water", notetree)
        notetree.show_notetree_gui()
