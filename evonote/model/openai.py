from __future__ import annotations
import openai
import os
from evonote import EvolverInstance

from evonote.data_type.var_types import ValueByInput

verbose = 1

'''
default_kwargs_cpl_openai = {"max_tokens": 1000, "model": "text-davinci-003"}


def cpl(prompt, **kwargs):
    """
    The function that calls the OpenAI API to generate text based on
    the prompt.
    :param prompt: The prompt to feed to the API
    :param use_cache: Whether to use cache
    :param cache_holder: The file path with which the cache is associated
    :param kwargs: Other arguments to pass to the OpenAI API
    :return:
    """
    input = str(prompt)
    options = {**default_kwargs_cpl_openai, **kwargs}
    func = lambda x: _cpl(x, options)

    _, _, stack = EvolverInstance.get_context()
    cache = EvolverInstance.read_cache(input, "cpl", stack[0].filename)
    if cache.value is not None:
        return ValueByInput.from_cache(cache, func)

    result_text = func(input)

    cache.set_cache(result_text)
    return ValueByInput.from_cache(cache, func)


def _cpl(prompt, options):
    return openai.Completion.create(prompt=prompt, **options).text.strip()

'''

# default_kwargs_chat_openai = {"model": "gpt-3.5-turbo"}
default_kwargs_chat_openai = {"model": "gpt-4"}


def _answer_0(messages, options):
    return openai.ChatCompletion.create(messages=messages, **options).choices[
        0].message.content


def _answer_1(chat: Chat, caller_path: str, **kwargs):
    input = chat.get_log_list()
    options = {**default_kwargs_chat_openai, **kwargs}
    func = lambda x: _answer_0(x, options)

    cache = EvolverInstance.read_cache(input, "chat", caller_path)
    if cache._value is not None:
        return ValueByInput.from_cache(cache, func)

    if verbose > 0:
        print("Asking the model:")
        print(input)

    result_text = func(input)
    chat.add_assistant_message(result_text)

    if verbose > 0:
        print("Response recieved:")
        print(result_text)

    cache.set_cache(result_text)
    return ValueByInput.from_cache(cache, func)


def answer(question: str, system_message: str = None, **kwargs):
    """
    One turn ask and answer
    :param question:
    :param system_message:
    :param kwargs:
    :return:
    """
    _, _, stack = EvolverInstance.get_context()
    chat = init_chat(question, system_message)
    return _answer_1(chat, stack[0].filename, **kwargs)


from evonote.data_type.chat import Chat


def init_chat(init_message: any, system_message: any = None) -> Chat:
    chat = Chat(system_message)
    chat.add_user_message(init_message)
    return chat


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

def get_embeddings(texts: list[str]) -> list[list[float]]:
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
        res = openai.Embedding.create(input=texts_without_cache,
                                      model=model_for_embedding)["data"]
        res = [r["embedding"] for r in res]

        for i, r in zip(index_for_eval, res):
            embedding_cache[hash_keys[i]] = r
            embeddings[i] = r

    np.save(embedding_cache_path, embedding_cache)

    return embeddings


def scores_in_context_lines(embedding_to_search, embedding_for_context_lines,
                            weighting=None):
    n_lines = len(embedding_for_context_lines)
    if weighting is None:
        weighting = np.array([1.0 / (i + 1) for i in range(n_lines)])
    content_embeddings = np.dot(weighting, embedding_for_context_lines)
    scores = np.dot(content_embeddings, embedding_to_search.T) / n_lines
    return scores
