from evonote.indexing.code_indexer import CodeDocsIndexer
from evonote.model.chat import Chat
from evonote.mindtree import Tree

"""
This module contains functions for searching in mind trees of python functions.
The python functions can be indexed by their docstrings, function names, parameter names, return values, etc.
"""

system_message = "You should output everything concisely as if you are a computer program"


def possible_function_names(description: str):
    prompt = "Give 3 possible function names for the following description."
    chat = Chat(user_message=prompt, system_message=system_message)
    chat.add_user_message("Description:\n" + description)
    chat.add_user_message(
        "Give the names with the underscore naming convention. Use newline to separate each name")
    res = chat.complete_chat()
    res = res.split("\n")
    res = [r.strip() for r in res]
    res = [" ".join(r.split("_")) for r in res if len(r) > 0]
    return res


def possible_docstring(description: str):
    prompt = "Give a possible docstring of for the function with the following description."
    prompt += "\nThe docstring should take only one-line."
    chat = Chat(user_message=prompt, system_message=system_message)
    chat.add_user_message("Description:\n" + description)
    chat.add_user_message("Start the answer with Docstring:")
    res = chat.complete_chat()
    ans_start = res.find(":")
    res = res[ans_start + 1:]
    return res


def search_function(description: str, tree: Tree, top_k=10):
    """
    Plan: TODO
    1. Imagine the docstring of the function by the description
    2. Imagine the function name by the description
    3. Imagine the parameter names by the description
    4. Imagine the return value by the description
    5. Search the tree by the above 4 things with CodeDocsIndexer, CodeParamIndexer, CodeReturnIndexer
    """

    names = possible_function_names(description)
    docstring = possible_docstring(description)
    query_keys = names + [docstring]
    return tree.get_sub_tree_by_similarity(query_keys, top_k=top_k,
                                           indexer_class=CodeDocsIndexer)
