from __future__ import annotations

from typing import List, TYPE_CHECKING

import openai

verbose = 1

if TYPE_CHECKING:
    from evonote.model.chat import Chat

default_kwargs_chat_openai = {"model": "gpt-3.5-turbo"}


def complete_chat(chat: Chat, options=None):
    _options = {**default_kwargs_chat_openai}
    if options is not None:
        _options.update(options)
    return openai.ChatCompletion.create(
        messages=chat.get_log_list(), **_options).choices[
        0].message.content


def complete_chat_expensive(chat: Chat, options=None):
    _options = {**default_kwargs_chat_openai}
    _options["model"] = "gpt-4"
    if options is not None:
        _options.update(options)
    return openai.ChatCompletion.create(
        messages=chat.get_log_list(), **_options).choices[
        0].message.content


import concurrent.futures


def complete_chat_parallel(chats: List[Chat], options=None):
    def complete_chat_wrapped(chat):
        return complete_chat(chat, options)

    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(complete_chat_wrapped, chat) for chat in chats]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            results.append(result)
    return results


# Embedding

import hashlib
import os
import numpy as np

model_for_embedding = "text-embedding-ada-002"
embedding_cache_path = os.getcwd() + "/embedding_cache.npy"
model_to_embedding_dim = {
    "text-embedding-ada-002": 1536
}
embedding_dim_using = model_to_embedding_dim[model_for_embedding]

embedding_cache = None


def flatten_nested_list(texts: list[list[str]], make_cache=False) \
        -> (List[float], List[int]):
    flattened_texts = []
    index_start = []
    for i, texts_ in enumerate(texts):
        index_start.append(len(flattened_texts))
        flattened_texts.extend(texts_)
    return flattened_texts, index_start


def get_embeddings(texts: list[str], make_cache=True) -> list[list[float]]:
    global embedding_cache
    if embedding_cache is None:
        if os.path.exists(embedding_cache_path):
            embedding_cache = np.load("embedding_cache.npy", allow_pickle=True).item()
        else:
            embedding_cache = {}

    hash_keys = [hashlib.md5(text.encode()).hexdigest() for text in texts]
    embeddings = []
    index_for_eval = []
    texts_without_cache = []
    for i, text in enumerate(texts):
        if hash_keys[i] not in embedding_cache:
            texts_without_cache.append(text)
            embeddings.append(None)
            index_for_eval.append(i)
        else:
            embeddings.append(embedding_cache[hash_keys[i]])
    if len(texts_without_cache) > 0:
        try:
            res = openai.Embedding.create(input=texts_without_cache,
                                          model=model_for_embedding)["data"]
        except Exception as e:
            print(e)
            print(texts_without_cache)
            raise e
        res = [r["embedding"] for r in res]
        print(f"{len(res)} embeddings generated")
        for i, r in zip(index_for_eval, res):
            embedding_cache[hash_keys[i]] = r
            embeddings[i] = r

    if make_cache:
        np.save(embedding_cache_path, embedding_cache)

    return embeddings


def cache_embeddings():
    global embedding_cache
    np.save(embedding_cache_path, embedding_cache)


def scores_in_context_lines(embedding_to_search, embedding_for_context_lines,
                            weighting=None):
    n_lines = len(embedding_for_context_lines)
    if weighting is None:
        weighting = np.array([1.0 / (i + 1) for i in range(n_lines)])
    content_embeddings = np.dot(weighting, embedding_for_context_lines)
    scores = np.dot(content_embeddings, embedding_to_search.T) / n_lines
    return scores
