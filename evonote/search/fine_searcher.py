from typing import List

import yaml

from evonote.file_helper.cache_manage import cache_manager, cached_function
from evonote.model.chat import Chat
from evonote.notebook.note import Note
from evonote.notebook.notebook import Notebook, new_notebook_from_note_subset

system_message = "You are a helpful processor for NLP problems. Output answer concisely as if you are a computer program."


def filter_note_by_note(note: Note, notebook: Notebook, criteria_prompt: str):
    note_path = note.get_note_path(notebook)
    cache_key = f"\nPath: {note_path}\nContent: {note.content}\n{criteria_prompt}"
    cache = cache_manager.read_cache(cache_key, "note_filtering")
    if cache.is_valid():
        return cache.value

    if len(note.content) > 0:
        prompt = f"You are working on filtering notes in a database according to its content and the path it is stored."
        prompt += f"\nPath: {note_path}\nContent: {note.content}"
    else:
        prompt = f"You are working on filtering notes in a database according to the path it is stored."
        prompt += f"\nPath: {note_path}"
    chat = Chat(
        user_message=prompt,
        system_message=system_message)
    asking_prompt = f" \n {criteria_prompt} \n Answer just Yes or No."
    chat.add_user_message(asking_prompt)

    res = chat.complete_chat()
    if "Yes" in res or "yes" in res:
        res = True
    elif "No" in res or "no" in res:
        res = False
    else:
        raise ValueError(f"Invalid answer: {res}")

    cache.set_cache(res)

    return res


def filter_notebook_note_by_note(notebook: Notebook, criteria_prompt: str) -> None:
    notes = notebook.get_all_notes()
    useless_notes = []
    for note in notes:
        if not filter_note_by_note(note, notebook, criteria_prompt):
            useless_notes.append(note)

    remove_happened = True
    while remove_happened:
        new_useless_notes = []
        remove_happened = False
        for note in useless_notes:
            if len(note.get_children(notebook)) == 0:
                notebook.remove_note(note)
                remove_happened = True
            else:
                new_useless_notes.append(note)
        useless_notes = new_useless_notes


@cached_function("notebook_filtering")
def filter_notebook_indices(notebook_yaml, criteria_prompt) -> \
        List[int]:
    prompt = f"You are working on filtering notes in a database according to its content and the path it is stored. The databased is stored in a YAML file, with each note labelled by an index." \
             f"\n{criteria_prompt}"
    chat = Chat(
        user_message=prompt,
        system_message=system_message)
    chat.add_user_message("The database: \n" + notebook_yaml)
    chat.add_user_message(
        f"Output the indices of the notes that satisfies the criteria with indices "
        f"separated by comma (output none when none matches): {criteria_prompt}.")
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


def filter_notebook_in_group(notebook: Notebook, criteria_prompt: str) -> Notebook:
    tree_with_indices, note_indexed = notebook.get_dict_with_indices_for_prompt()
    tree_in_yaml = yaml.dump(tree_with_indices)
    useful_indices = filter_notebook_indices(tree_in_yaml, criteria_prompt)
    useful_notes = [note_indexed[i] for i in useful_indices]
    filtered = new_notebook_from_note_subset(useful_notes, notebook)
    return filtered


def keyword_filter(notebook: Notebook, keywords: List[str]):
    if len(keywords) > 1:
        prompt = "The note is related to all of the following keywords: " + ",".join(
            keywords)
    else:
        prompt = "The note is related to the following keyword: " + keywords[0]
    return filter_notebook_in_group(notebook,
                                    prompt)
