import concurrent
import math

from evonote import EvolverInstance
from evonote.core.embed_indexer import EmbedIndexer
from evonote.core.note import Note, Notebook
from evonote.file_helper.evolver import save_cache
from evonote.model.llm import complete_chat

import numpy as np

prompt_for_splitting = "Split the following sentence into smaller fragments (no more than about 8 words). Put each fragment in a new line."
prompt_for_extracting = "Give some key phrases for the following sentence to be searched (no more than about 8 words). Put each key phrase in a new line."
def process_sent_into_frags(sent: str, use_cache=True, caller_path=None, prompt=prompt_for_splitting):
    if caller_path is None:
        caller_path = EvolverInstance.get_caller_path()
    cache = EvolverInstance.read_cache(sent, "sent_breaking",
                                       caller_path, True)
    if use_cache:
        if cache.is_valid():
            return cache._value

    system_message = "You are a helpful processor for NLP problems. Answer anything concisely and parsable. Use newline to separate multiple answers."
    from evonote.data_type.chat import Chat
    chat = Chat(
        user_message=prompt,
        system_message=system_message)
    chat.add_user_message(sent)
    res = complete_chat(chat)
    res = res.split('\n')

    # filter out empty lines
    res = [line for line in res if len(line.strip()) != 0]

    if res[0][0] == "-":
        for i in range(len(res)):
            if res[i][0] == "-":
                res[i] = res[i][1:].strip()

    for i in range(len(res)):
        if "," in res[i]:
            keys = res[i].split(",")
            res[i] = keys[0]
            res.extend(keys[1:])

    res = [line for line in res if len(line.strip()) != 0]

    cache.set_cache(res)

    return res


def default_indexing(notebook: Notebook, use_cache=True,
                     caller_path=None):
    caller_path = caller_path if caller_path is not None else EvolverInstance.get_caller_path()

    break_sent_use_cache = lambda sent: process_sent_into_frags(sent, use_cache,
                                                                caller_path)
    notebook.indexer_class = EmbedIndexer

    #children = notebook.get_all_notes()
    children = notebook.notes_without_indexer
    children_content = []
    children_non_empty = []
    children_empty = []
    for child in children:
        if len(child.content) == 0:
            continue
        children_content.append(child.content)
        children_non_empty.append(child)
        children_empty.append(child)

    for child in children_empty:
        indexer: EmbedIndexer = notebook.get_indexer(child)
        keywords_on_path = child.get_note_path(notebook)
        if len(keywords_on_path) != 0:
            # keep last 1/3 of the keywords
            n_keywords = min(max(math.ceil(len(keywords_on_path) / 3), 3), len(keywords_on_path))
            indexer.src_list.extend(keywords_on_path[-n_keywords:])
            weight = np.array([i+1 for i in range(len(indexer.src_list))])
            weight = weight / np.sum(weight)
            indexer.src_weight = weight
        indexer.src_list.append(child.content)

    n_finished = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        for child, frags in zip(children_non_empty,
                                executor.map(break_sent_use_cache, children_content)):
            indexer: EmbedIndexer = notebook.get_indexer(child)
            indexer.src_list.extend(frags)
            indexer.src_list.append(child.get_note_path(notebook)[-1])
            indexer.src_list.append(child.content)

            n_finished += 1
            if n_finished % 20 == 19:
                save_cache()
    save_cache()

    notebook.notes_without_indexer = []
