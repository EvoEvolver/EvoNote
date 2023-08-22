import concurrent
import math

from evonote import EvolverInstance
from evonote.core.embed_indexer import EmbedIndexer
from evonote.core.note import Note, Notebook
from evonote.file_helper.evolver import save_cache
from evonote.model.llm import complete_chat


def break_sent_into_frags(sent: str, use_cache=True, caller_path=None):
    if caller_path is None:
        _, _, stack = EvolverInstance.get_context()
        caller_path = stack[0].filename
    cache = EvolverInstance.read_cache(sent, "sent_breaking",
                                       caller_path, True)
    if use_cache:
        if cache.is_valid():
            return cache._value

    system_message = "You are a helpful processor for NLP problems. Answer anything concisely and parsable."
    from evonote.data_type.chat import Chat
    chat = Chat(
        user_message="Split the following sentence into smaller fragments (no more than about 8 words). Put each fragment in a new line.",
        system_message=system_message)
    chat.add_user_message(sent)
    res = complete_chat(chat)
    res = res.split('\n')

    # filter out empty lines
    res = [line for line in res if len(line.strip()) != 0]

    if res[0][0] != "-":
        cache.set_cache(res)
        return res

    for i in range(len(res)):
        if res[i][0] == "-":
            res[i] = res[i][1:].strip()

    cache.set_cache(res)

    return res


def make_frag_indexing(note: Note, use_cache=True, notebook: Notebook = None,
                       caller_path=None):
    caller_path = caller_path if caller_path is not None else EvolverInstance.get_caller_path()

    break_sent_use_cache = lambda sent: break_sent_into_frags(sent, use_cache,
                                                              caller_path)
    notebook = notebook if notebook is not None else note.default_notebook
    notebook.indexer_class = EmbedIndexer

    children = note.get_descendants(notebook=notebook)
    children_content = []
    children_non_empty = []
    for child in children:
        if len(child.content) == 0:
            continue
        children_content.append(child.content)
        children_non_empty.append(child)

    n_finished = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        for child, frags in zip(children_non_empty,
                                executor.map(break_sent_use_cache, children_content)):
            indexer: EmbedIndexer = notebook.get_indexer(child)
            indexer.src_list.extend(frags)

            keywords_on_path = child.get_note_path(notebook)
            if len(keywords_on_path) != 0:
                # keep last 1/3 of the keywords
                n_keywords = math.ceil(len(keywords_on_path) / 3)
                indexer.src_list.extend(keywords_on_path[-n_keywords:])
            indexer.src_list.append(child.content)

            n_finished += 1
            if n_finished % 20 == 19:
                save_cache()
    save_cache()
