from evonote.transform.module_to_notebook.extract_from_module import get_notebook_for_module
from evonote.debug import display_chats, display_embedding_search
from evonote.search.code_searcher import search_function
from evonote.testing.testing_modules import v_lab

notebook = get_notebook_for_module(v_lab)

with display_embedding_search():
    with display_chats():
        notebook = search_function("Add water", notebook)
        notebook.show_notebook_gui()
