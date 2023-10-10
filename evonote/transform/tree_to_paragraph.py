import json

from evonote.file_helper.cache_manage import cached_function
from evonote.model.chat import Chat
from evonote.mindtree import Tree

@cached_function("tree_to_paragraph")
def _tree_to_paragraph_impl(dict_for_prompt: str, writing_instruction: str):
    chat = Chat(
        system_message="You are a excellent writer who can transform JSON to a coherent paragraph so human can read it.")
    chat.add_user_message(
        "Please transform the following JSON generated from a knowledge database to a paragraph that can be read by human."
        "\n JSON: \n" + dict_for_prompt +
        f""" 
You should focus more on presenting the `content` of the JSON than the keys.
{writing_instruction}
Start your answer with `Paragraph:`
""")
    res = chat.complete_chat()
    return res

def tree_to_paragraph(tree: Tree, writing_instruction: str):
    dict_for_prompt = tree.get_dict_for_prompt()
    dict_for_prompt = json.dumps(dict_for_prompt, indent=1)
    res = _tree_to_paragraph_impl(dict_for_prompt, writing_instruction)
    return res
