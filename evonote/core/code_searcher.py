from evonote.core.note import Notebook
from evonote.data_type.chat import Chat
from evonote.model.llm import complete_chat

system_message = "You should output everything concisely as if you are a computer program"

def possible_function_names(description: str):
    prompt = "Give 3 possible function names for the following description."
    chat = Chat(user_message=prompt, system_message=system_message)
    chat.add_user_message("Description:\n" + description)
    chat.add_user_message("Give the names with the underscore naming convention. Use newline to separate each name")
    res = complete_chat(chat)
    res = res.split("\n")
    res = [r.strip() for r in res]
    res = [r for r in res if len(r) > 0]
    return res

def possible_docstring(description: str):
    prompt = "Give a possible docstring of for the function with the following description."
    prompt += "\nThe docstring should take only one-line."
    chat = Chat(user_message=prompt, system_message=system_message)
    chat.add_user_message("Description:\n" + description)
    chat.add_user_message("Start the answer with Docstring:")
    res = complete_chat(chat)
    ans_start = res.find(":")
    res = res[ans_start+1:]
    return res

def search_function(description: str, notebook: Notebook):
    names = possible_function_names(description)
    docstring = possible_docstring(description)
    query_keys = names + [docstring]
    notebook.sub_notebook_by_similarity(query_keys, top_k=2, type_filter="code:function").show_notebook_gui()
