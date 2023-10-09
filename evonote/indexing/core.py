from __future__ import annotations

import concurrent
import math
from typing import List, Type, Any, Callable, TYPE_CHECKING

import numpy as np

from evonote.file_helper.logger import Logger
from evonote.model.chat import Chat

if TYPE_CHECKING:
    from evonote.notetree import Note
    from evonote.notetree import Tree

from evonote.file_helper.cache_manage import save_cache, cached_function
from evonote.model.openai import get_embeddings


class Indexer:
    """
    An indexer is a class that takes in a list of notes and returns a data structure that
    can be used to compute similarities between notes.

    Indexer is stateless and its state is stored in the Indexing object.
    """

    @classmethod
    def make_data(cls, notes: List[Note], indexing: Indexing):
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
                 notetree: Tree):
        self.notes_without_indexer: List[Note] = notes[:]
        self.indexer: Type[Indexer] = indexer
        self.data: Any = None
        self.notetree = notetree

    def add_new_note(self, note: Note):
        self.notes_without_indexer.append(note)

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


class Query:
    def __init__(self, query, query_type: str = "similarity"):
        """
        :param query: The content of the query
        :param query_type: The type of the query. It can be "similarity" or "question" or any other type the indexer supports
            if the indexer does not support the query type, it will treat it as a similarity query
        """
        self.query = query
        self.query_type = query_type


class IndexingSearchLogger(Logger):
    active_loggers = []

    def display_log(self):
        from evonote.gui.similarity_search import draw_similarity_gui
        for log in self.log_list:
            draw_similarity_gui(*log)


class AbsEmbeddingIndexer(Indexer):
    @classmethod
    def prepare_src_weight_list(cls, new_notes: List[Note], indexing: Indexing,
                                ) -> (
            List[List[str]], List[List[float]], List[Note]):
        """
        Select notes that will be indexed and return a list of srcs and weights for each
        :param new_notes: The incoming notes
        :param indexing: The indexing object
        :return: A triplet of srcs, weights, and notes
        """
        raise NotImplementedError

    @classmethod
    def make_data(cls, new_notes: List[Note], indexing: Indexing):
        if indexing.data is None:
            indexing.data = {
                "vecs": None,
                "srcs_list": [],
                "note_of_vecs": [],
                "weights_list": [],
            }

        new_srcs, new_weights, new_note_of_vecs = cls.prepare_src_weight_list(new_notes,
                                                                              indexing)
        indexing.data["srcs_list"].extend(new_srcs)
        indexing.data["note_of_vecs"].extend(new_note_of_vecs)
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

        for i, start_index in enumerate(children_index_start):
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
        if len(vecs) == 0:
            return [], []

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

        if len(IndexingSearchLogger.active_loggers) > 0:
            IndexingSearchLogger.add_log_to_all(
                show_src_similarity_gui(similarity, indexing.data, query, weights))

        return similarity, indexing.data["note_of_vecs"]

    @classmethod
    def process_note_with_content(cls, notes: List[Note], indexing: Indexing,
                                  ):
        raise NotImplementedError

    @classmethod
    def process_note_without_content(cls, notes: List[Note], indexing: Indexing,
                                     ):
        raise NotImplementedError


def show_src_similarity_gui(similarity, data, query, weights, top_k=10):
    top_note_index = np.argsort(similarity)[::-1][:top_k]
    notes = data["note_of_vecs"]
    top_notes = [notes[i] for i in top_note_index]
    contents = [note.content for note in top_notes]
    src_list = data["srcs_list"]
    src_list = [src_list[i] for i in top_note_index]
    return src_list, weights, query, contents


class FragmentedEmbeddingIndexer(AbsEmbeddingIndexer):
    @classmethod
    def process_note_with_content(cls, notes: List[Note], indexing: Indexing,
                                  ):
        notes_content = [note.content for note in notes]
        notetree = indexing.notetree

        new_src_list = []
        new_weights = []
        n_finished = 0
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            for note, frags in zip(notes,
                                   executor.map(process_sent_into_frags, notes_content)):
                new_src = []
                new_src.extend(frags)
                note_path = notetree.get_note_path(note)
                if len(note_path) > 0:
                    new_src.append(notetree.get_note_path(note)[-1])
                new_src.append(note.content)

                new_src_list.append(new_src)
                # TODO Handle when there are too many fragments. Maybe we should group
                #  them by clustering
                weight = np.ones(len(new_src)) / (len(new_src) ** 0.95)
                new_weights.append(weight)

                n_finished += 1
                if n_finished % 20 == 19:
                    save_cache()

        save_cache()
        return new_src_list, new_weights

    @classmethod
    def process_note_without_content(cls, notes: List[Note], indexing: Indexing,
                                     ):
        new_src_list = []
        new_weights = []

        for note in notes:
            keywords_on_path = note.note_path()
            # keep last 1/3 of the keywords
            n_keywords = min(max(math.ceil(len(keywords_on_path) / 3), 3),
                             len(keywords_on_path))
            new_src = keywords_on_path[-n_keywords:]
            new_src_list.append(new_src)
            weight = np.array([i + 1 for i in range(len(new_src))])
            weight = weight / np.sum(weight)
            new_weights.append(weight)

        return new_src_list, new_weights

    @classmethod
    def prepare_src_weight_list(cls, new_notes: List[Note], indexing: Indexing,
                                ):

        notetree = indexing.notetree
        notes_with_content = []
        notes_content = []
        notes_without_content = []
        for note in new_notes:
            if len(note.content) == 0:
                keywords_on_path = notetree.get_note_path(note)
                if len(keywords_on_path) != 0:
                    notes_without_content.append(note)
                continue
            notes_with_content.append(note)
            notes_content.append(note.content)

        new_src_list_1, new_weights_1 = cls.process_note_without_content(
            notes_without_content, indexing)

        new_src_list_2, new_weights_2 = cls.process_note_with_content(
            notes_with_content, indexing)

        new_src_list = new_src_list_1 + new_src_list_2
        new_weights = new_weights_1 + new_weights_2
        new_notes = notes_without_content + notes_with_content

        assert len(new_src_list) == len(new_weights) == len(new_notes)

        return new_src_list, new_weights, new_notes


prompt_for_splitting = "Split the following sentence into smaller fragments (no more than about 8 words). Put each fragment in a new line."
prompt_for_extracting = "Give some phrases that summarize the following sentence. The phrases should be no more than 8 words and represents what the sentence is describing. Put each phrase in a new line."

@cached_function("sent_breaking")
def process_sent_into_frags(sent: str,
                            prompt=prompt_for_extracting):

    system_message = ("You are a helpful processor for NLP problems. Answer anything "
                      "concisely and parsable. Use newline to separate multiple answers.")

    chat = Chat(
        user_message=prompt,
        system_message=system_message)
    chat.add_user_message("Sentence: "+sent)
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

    return res
