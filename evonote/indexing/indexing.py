from __future__ import annotations

import concurrent
import math
from typing import List, Type, Any, Callable, TYPE_CHECKING

from evonote.core.utils import get_main_path

if TYPE_CHECKING:
    from evonote.core.note import Note, Notebook

from evonote import EvolverInstance

from evonote.file_helper.evolver import save_cache
from evonote.model.llm import get_embeddings, complete_chat


class Indexer:
    """
    An indexer is a class that takes in a list of notes and returns a data structure that
    can be used to compute similarities between notes.

    Indexer is stateless and its state is stored in the Indexing object.
    """

    @classmethod
    def make_data(cls, notes: List[Note], indexing: Indexing, use_cache: bool = True):
        raise NotImplementedError

    @classmethod
    def get_similarities(cls, query: List[str], indexing: Indexing,
                         weights: List[float] = None):
        raise NotImplementedError

    @classmethod
    def remove_note(cls, note: Note):
        raise NotImplementedError


class Indexing:
    def __init__(self, notes: List[Note], indexer: Type[Indexer],
                 notebook: Notebook):
        self.notes_without_indexer: List[Note] = notes[:]
        self.indexer: Type[Indexer] = indexer
        self.data: Any = None
        self.notebook = notebook

    def add_new_note(self, note: Note):
        self.notes_without_indexer.append(note)
        self.indexer.remove_note(note)

    def remove_note(self, note: Note):
        if note in self.notes_without_indexer:
            self.notes_without_indexer.remove(note)

    def make_data(self):
        self.indexer.make_data(self.notes_without_indexer, self)

    def get_similarities(self, query: List[str], weights: List[float] = None) -> (
            List[float], List[Note]):
        if len(self.notes_without_indexer) > 0:
            self.make_data()
        return self.indexer.get_similarities(query, self, weights)

    def get_top_k_notes(self, query: List[str], weights: List[float] = None, k: int = 10,
                        note_filter: Callable[[Note], bool] = None) -> List[Note]:
        similarities, notes = self.get_similarities(query, weights)
        note_rank = np.argsort(similarities)[::-1]
        note_added = set()
        top_k_notes = []
        note_filter = note_filter if note_filter is not None else lambda note: True
        for i in range(len(note_rank)):
            note = notes[note_rank[i]]
            if note not in note_added and note_filter(note):
                top_k_notes.append(note)
                note_added.add(note)
            if len(top_k_notes) == k:
                break
        return top_k_notes


import numpy as np


class AbsEmbeddingIndexer(Indexer):
    @classmethod
    def prepare_src_weight_list(cls, new_notes: List[Note], indexing: Indexing,
                                use_cache: bool) -> (
    List[List[str]], List[List[float]], List[Note]):
        raise NotImplementedError

    @classmethod
    def make_data(cls, new_notes: List[Note], indexing: Indexing,
                  use_cache: bool = True):
        if indexing.data is None:
            indexing.data = {
                "vecs": None,
                "srcs_list": [],
                "index_to_note": [],
                "weights_list": [],
            }

        new_srcs, new_weights, new_index_to_note = cls.prepare_src_weight_list(new_notes,
                                                                               indexing,
                                                                               use_cache)
        indexing.data["srcs_list"].extend(new_srcs)
        indexing.data["index_to_note"].extend(new_index_to_note)
        indexing.data["weights_list"].extend(new_weights)

        new_vecs = []
        flattened_src_list = []
        flattened_weight_list = []

        children_index_start = []
        for i, srcs in enumerate(new_srcs):
            if len(srcs) == 0:
                children_index_start.append(-1)
                continue
            children_index_start.append(len(flattened_src_list))
            flattened_src_list.extend(srcs)
            flattened_weight_list.extend(new_weights[i])

        src_embedding_list = np.array(get_embeddings(flattened_src_list, make_cache=True))

        weighted_embeddings = (src_embedding_list.T * np.array(
            flattened_weight_list)).T

        embedding_dim = len(src_embedding_list[0])

        for i, start_index in enumerate(children_index_start[:-1]):
            if start_index == -1:
                new_vecs.append(np.zeros(embedding_dim))
                continue
            child_embedding_list = weighted_embeddings[start_index: start_index + len(
                new_srcs[i])]
            new_vecs.append(
                np.sum(child_embedding_list, axis=0))

        # Merge new_vecs with existing vecs

        new_vecs = np.array(new_vecs)
        if indexing.data["vecs"] is None:
            indexing.data["vecs"] = np.array(new_vecs)
        else:
            existing_vecs = indexing.data["vecs"]
            concatenated_vecs = np.concatenate([existing_vecs, new_vecs])
            indexing.data["vecs"] = concatenated_vecs

    @classmethod
    def get_similarities(cls, query: List[str], indexing: Indexing,
                         weights: List[float] = None) -> (List[float], List[Note]):

        text_embedding_list = get_embeddings(query, make_cache=True)
        vecs = indexing.data["vecs"]

        text_embedding_list = np.array(text_embedding_list)
        similarity = vecs.dot(text_embedding_list.T).T

        if weights is None:
            weights = [1.0] * len(vecs)

        average_similarity = np.average(similarity, axis=1)
        similarity = similarity.T - average_similarity - 0.05
        # add non-linearity to similarity
        similarity = np.exp(similarity * 2)
        similarity = similarity * weights

        similarity = np.sum(similarity, axis=1)

        return similarity, indexing.data["index_to_note"]


class FragmentedEmbeddingIndexer(AbsEmbeddingIndexer):
    @classmethod
    def prepare_src_weight_list(cls, new_notes: List[Note], indexing: Indexing,
                                use_cache: bool):

        notebook = indexing.notebook

        index_to_note = []

        notes_with_content = []
        notes_content = []
        notes_without_content = []
        for note in new_notes:
            if len(note.content) == 0:
                keywords_on_path = note.get_note_path(notebook)
                if len(keywords_on_path) != 0:
                    notes_without_content.append(note)
                continue
            notes_with_content.append(note)
            notes_content.append(note.content)

        new_src_list_1 = []
        new_weights_1 = []

        for note in notes_without_content:
            keywords_on_path = note.get_note_path(notebook)
            # keep last 1/3 of the keywords
            n_keywords = min(max(math.ceil(len(keywords_on_path) / 3), 3),
                             len(keywords_on_path))
            new_src = keywords_on_path[-n_keywords:]
            new_src_list_1.append(new_src)
            weight = np.array([i + 1 for i in range(len(new_src))])
            weight = weight / np.sum(weight)
            new_weights_1.append(weight)

        break_sent_use_cache = lambda sent: process_sent_into_frags(sent, use_cache,
                                                                    get_main_path())

        new_src_list_2 = []
        new_weights_2 = []
        n_finished = 0
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            for note, frags in zip(notes_with_content,
                                   executor.map(break_sent_use_cache, notes_content)):
                new_src = []
                new_src.extend(frags)
                note_path = note.get_note_path(notebook)
                if len(note_path) > 0:
                    new_src.append(note.get_note_path(notebook)[-1])
                new_src.append(note.content)

                new_src_list_2.append(new_src)
                weight = np.ones(len(new_src)) / (len(new_src) ** 0.8)
                new_weights_2.append(weight)

                n_finished += 1
                if n_finished % 20 == 19:
                    save_cache()

        save_cache()

        new_src_list = new_src_list_1 + new_src_list_2
        new_weights = new_weights_1 + new_weights_2
        new_notes = notes_without_content + notes_with_content

        assert len(new_src_list) == len(new_weights) == len(new_notes)

        return new_src_list, new_weights, new_notes


prompt_for_splitting = "Split the following sentence into smaller fragments (no more than about 8 words). Put each fragment in a new line."
prompt_for_extracting = "Give some phrases that summarize the following sentence. The phrases should be no more than 8 words and represents what the sentence is describing. Put each phrase in a new line."


def process_sent_into_frags(sent: str, use_cache=True, caller_path=None,
                            prompt=prompt_for_extracting):
    if caller_path is None:
        caller_path = EvolverInstance.get_caller_path()
    cache = EvolverInstance.read_cache(sent, "sent_breaking",
                                       caller_path, True)
    if use_cache:
        if cache.is_valid():
            return cache._value

    system_message = "You are a helpful processor for NLP problems. Answer anything concisely and parsable. Use newline to separate multiple answers."
    from evonote.model.chat import Chat
    chat = Chat(
        user_message=prompt,
        system_message=system_message)
    chat.add_user_message(sent)
    res = chat.complete_chat()
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
