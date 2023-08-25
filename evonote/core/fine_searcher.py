from evonote import EvolverInstance
from evonote.core.note import Notebook, Note
from evonote.data_type.chat import Chat
from evonote.model.llm import complete_chat, complete_chat_expensive

system_message = "You are a helpful processor for NLP problems. Output answer concisely as if you are a computer program."

def filter_note(note: Note, notebook: Notebook, criteria_prompt: str, caller_path: str, use_cache=True):

    note_path = note.get_note_path(notebook)
    cache_key = f"\nPath: {note_path}\nContent: {note.content}\n{criteria_prompt}"
    cache = EvolverInstance.read_cache(cache_key, "note_filtering", caller_path, True)
    if use_cache:
        if cache.is_valid():
            return cache._value

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

    res = complete_chat(chat)
    if "Yes" in res or "yes" in res:
        res = True
    elif "No" in res or "no" in res:
        res = False
    else:
        raise ValueError(f"Invalid answer: {res}")

    cache.set_cache(res)

    return res


def filter_notebook_0(notebook: Notebook, criteria_prompt: str, caller_path=None, use_cache=True):
    if caller_path is None:
        caller_path = EvolverInstance.get_caller_path()
    notes = notebook.get_all_notes()
    useless_notes = []
    for note in notes:
        if not filter_note(note, notebook, criteria_prompt, caller_path, use_cache=use_cache):
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

def filter_notebook_indices(notebook_yaml, criteria_prompt, caller_path, use_cache):
    cache_key = f"\n{notebook_yaml}\n{criteria_prompt}"
    cache = EvolverInstance.read_cache(cache_key, "notebook_filtering",
                                       caller_path, True)
    if use_cache:
        if cache.is_valid():
            return cache._value

    prompt = f"You are working on filtering notes in a database according to its content and the path it is stored. The databased is stored in a YAML file, with each note labelled by an index." \
             f"\n{criteria_prompt}"
    chat = Chat(
        user_message=prompt,
        system_message=system_message)
    chat.add_user_message("The database: \n" + notebook_yaml)
    chat.add_user_message(
        f"Output the indices of the notes that satisfies the criteria with indices saperated by comma: {criteria_prompt}.")
    res = complete_chat(chat)
    try:
        useful_indices = [int(i.strip()) for i in res.split(",")]
    except:
        raise ValueError(f"Invalid answer: {res}")
    cache.set_cache(useful_indices)

    return useful_indices

def filter_notebook_1(notebook: Notebook, criteria_prompt: str, caller_path=None, use_cache=True):
    if caller_path is None:
        caller_path = EvolverInstance.get_caller_path()
    yaml, note_indexed = notebook.get_yaml_for_prompt()
    useful_indices = filter_notebook_indices(yaml, criteria_prompt, caller_path, use_cache)
    useful_notes = [note_indexed[i] for i in useful_indices]
    useless_notes = notebook.get_all_notes()
    for note in useful_notes:
        useless_notes.remove(note)
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