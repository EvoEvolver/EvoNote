import evonote.debug as debug
from evonote.model.chat import Chat
from evonote.notetree import Tree


def some_function():
    chat = Chat(system_message="You are a helpful assistant.")
    chat.add_user_message("Count from 1 to 10.")
    res = chat.complete_chat()
    print(res)


with debug.display_chats():
    some_function()

def example_notetree():
    notetree = Tree("notetree for testing")
    notetree.get_new_note_by_path(["People", "Mike"]).be("Mike lives in Los Santos")
    notetree.get_new_note_by_path(["Fruit", "Apple"]).be("Apple is a fruit")
    return notetree


# <- Set a break point here
notetree = example_notetree()
notetree.show_notetree_gui()

# <- Set a break point here
with debug.display_embedding_search():
    with debug.display_chats():
        with debug.refresh_cache():
            sub_notetree = notetree.get_sub_notetree_by_similarity(
                ["Franklin lives in Los Santos"], top_k=1)
            sub_notetree.show_notetree_gui()
