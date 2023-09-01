from typing import List

from evonote.core.note import Note
from evonote.core.notebook import Notebook
from evonote.core.utils import robust_json_parse
from evonote.model.chat import Chat

system_message = "Reply everything concisely without explaination as if you are a computer program."


def generate_possible_keywords(content: str, context: str):
    prompt = "You are managing a database of notes."
    prompt += "You are trying to find a path to put a new note based on its content and context."
    prompt += f"\nContent: {content}"
    if len(context) > 0:
        prompt += f"\nContext: {context}"
    chat = Chat(user_message=prompt, system_message=system_message)
    chat.add_user_message(
        "Output 2 keywords that are important and independent. Separate each keyword by newline.")
    res = chat.complete_chat_expensive()
    res = res.split("\n")
    res = [r.strip() for r in res]
    res = [r for r in res if len(r) > 0]
    return res


def search_similar_paths(keywords, notebook: Notebook):
    notes = notebook.get_notes_by_similarity(keywords, top_k=5)
    similar_paths = [note.get_note_path(notebook) for note in notes]
    return similar_paths


def conceive_path(content: str, context: str, similar_paths: List[List[str]]):
    prompt = "You are managing a database of notes."
    prompt += "You are trying to find a path to put a new note based on its content and context."
    prompt += f"\nContent: {content}"
    if len(context) > 0:
        prompt += f"\nContext: {context}"
    chat = Chat(user_message=prompt, system_message=system_message)
    path_prompt = ["Here are some related paths to put the note.\n"]
    for i, path in enumerate(similar_paths):
        path_prompt.append("/".join(path))
    path_prompt.append("")
    path_prompt.append(
        "Output a path that is proper to put the note. You can create new path, but you should avoid it with possible. Start with `Path:`")
    path_prompt = "\n".join(path_prompt)
    chat.add_user_message(path_prompt)
    res = chat.complete_chat()
    start = res.find(":")
    res = res[start + 1:].strip()
    res = res.split("/")
    return res


def put_content_to_notebook_1(content: str, context: str, path_to_put,
                              notebook: Notebook):
    chat = Chat(system_message=system_message)

    prompt = "You are managing a database of notes."
    prompt += "You want to put the following note to the database."
    prompt += f"\nContent: {content}"
    if len(context) > 0:
        prompt += f"\nContext: {context}"
    chat.add_user_message(prompt)

    prompt_adding = "You want to add the above note to the following path."
    prompt_adding += f"\nCurrent Path: {path_to_put.join('/')}"
    note_in_path = notebook.get_note_by_path(path_to_put)

    if len(note_in_path.content) > 0:
        prompt_adding += f"\nContent in current path: {note_in_path.content}"

    # Also show the content in parent path if it is not empty
    note_in_parent_path = notebook.get_note_by_path(path_to_put[:-1])
    if len(note_in_parent_path.content) > 0:
        prompt_adding += f"\nParent path: {path_to_put[:-1].join('/')}"
        prompt_adding += f"\nContent in parent path: {note_in_parent_path.content}"

    chat.add_user_message(prompt_adding)

    prompt_confirm = "Is that more proper to put the note in the current path, the parent path or "
    prompt_confirm += "\nOutput `current` or `parent`"
    chat.add_user_message(prompt_confirm)

    res = chat.complete_chat()

    # TODO not finished


def put_content_to_notebook(content: str, context: str, path_to_put, notebook: Notebook):
    chat = Chat(system_message=system_message)

    prompt_adding = "You are managing a database of notes."
    prompt_adding += "\nYou want to add the a note to the following path."
    prompt_adding += f"\nCurrent Path: {'/'.join(path_to_put)}"
    note_in_path = notebook.get_note_by_path(path_to_put)

    if note_in_path is not None and len(note_in_path.content) > 0:
        prompt_adding += f"\nContent in current path: {note_in_path.content}"

    chat.add_user_message(prompt_adding)

    prompt_note = "Here is a note you want to add."
    prompt_note += f"\nContent: {content}"
    if len(context) > 0:
        prompt_note += f"\nContext: {context}"
    chat.add_user_message(prompt_note)

    prompt_asking = "Considering the context might have been included in the parent paths. " \
                    "Give a title for the content to be stored in the current path." \
                    "Based on the filename, give the altered content to be stored in the current path." \
                    "\n Output the result in JSON with key `title` and `new content`"

    chat.add_user_message(prompt_asking)

    res = chat.complete_chat()

    res = robust_json_parse(res)

    filename = res["title"]
    new_content = res["new content"]
    path_for_new_note = path_to_put + [filename]
    new_note = Note(notebook)
    new_note.content = new_content
    print(filename, new_content, path_for_new_note)

    notebook.add_note_by_path(path_for_new_note, new_note)


def add_content_to_notebook(content: str, context: str, notebook: Notebook):
    # step 1: generate possible keywords
    # step 2: search related paths / notes
    # step 3: decide a path to put content
    keywords = generate_possible_keywords(content, context)
    similar_paths = search_similar_paths(keywords, notebook)
    conceived_path = conceive_path(content, context, similar_paths)
    print(conceived_path)
    put_content_to_notebook(content, context, conceived_path, notebook)


if __name__ == "__main__":
    content = "Quantum computing can offer exponential speedup for certain problems."
    context = ""
    keywords = generate_possible_keywords(content, context)
    print(keywords)
