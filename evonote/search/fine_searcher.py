from typing import List

import yaml

from evonote.file_helper.cache_manage import cached_function
from evonote.model.chat import Chat
from evonote.notetree.tree import Tree, new_notetree_from_note_subset

"""
This module is for fine-grained search. The object notetree will be put in the prompt and LLM can select useful notes by a certain criteria.
However, fine-grained search should not be adopted because it is slow and expensive.
"""

system_message = "You are a helpful processor for NLP problems. Output answer concisely as if you are a computer program."

@cached_function("notetree_filtering")
def filter_notetree_indices(notetree_yaml, criteria_prompt) -> \
        List[int]:
    prompt = f"You are working on filtering notes in a database according to its content and the path it is stored. The databased is stored in a YAML file, with each note labelled by an index." \
             f"\n{criteria_prompt}"
    chat = Chat(
        user_message=prompt,
        system_message=system_message)
    chat.add_user_message("The database: \n" + notetree_yaml)
    chat.add_user_message(
        f"Output the indices of the notes that satisfies the criteria with indices "
        f"separated by comma (output none when none matches): \n"
        f"{criteria_prompt}.")
    res = chat.complete_chat_expensive()
    original_res = res
    if "none" in res or "None" in res:
        return []
    number_start = -1
    for i in range(len(res)):
        if res[i] in "0123456789":
            number_start = i
            break
    if number_start == -1:
        raise ValueError(f"Invalid answer: {res}")
    number_end = len(res)
    for i in range(number_start, len(res)):
        if res[i] not in "0123456789, ":
            number_end = i
            break
    res = res[number_start:number_end]
    try:
        useful_indices = [int(i.strip()) for i in res.split(",")]
    except Exception as e:
        raise ValueError(f"Invalid answer: {res}, {original_res}")

    return useful_indices


def filter_notetree_in_group(notetree: Tree, criteria_prompt: str) -> Tree:
    tree_with_indices, note_indexed = notetree.get_dict_with_indices_for_prompt()
    tree_in_yaml = yaml.dump(tree_with_indices)
    useful_indices = filter_notetree_indices(tree_in_yaml, criteria_prompt)
    useful_notes = [note_indexed[i] for i in useful_indices]
    filtered = new_notetree_from_note_subset(useful_notes, notetree)
    return filtered


def keyword_filter(notetree: Tree, keywords: List[str]):
    if len(keywords) > 1:
        prompt = "The note is related to all of the following keywords: " + ",".join(
            keywords)
    else:
        prompt = "The note is related to the following keyword: " + keywords[0]
    return filter_notetree_in_group(notetree,
                                    prompt)
