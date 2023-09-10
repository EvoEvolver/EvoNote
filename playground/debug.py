import evonote.debug as debug
from evonote.model.chat import Chat
from evonote.notebook.notebook import Notebook


def some_function():
    chat = Chat(system_message="You are a helpful assistant.")
    chat.add_user_message("Count from 1 to 10.")
    res = chat.complete_chat()
    print(res)


with debug.display_chats():
    some_function()

def example_notebook():
    notebook = Notebook("notebook for testing")
    notebook.get_new_note_by_path(["People", "Mike"]).be("Mike lives in Los Santos")
    notebook.get_new_note_by_path(["Fruit", "Apple"]).be("Apple is a fruit")
    return notebook


# <- Set a break point here
notebook = example_notebook()
notebook.show_notebook_gui()

# <- Set a break point here
with debug.display_embedding_search():
    with debug.display_chats():
        with debug.refresh_cache():
            sub_notebook = notebook.get_sub_notebook_by_similarity(
                ["Franklin lives in Los Santos"], top_k=1)
            sub_notebook.show_notebook_gui()
