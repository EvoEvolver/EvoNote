from __future__ import annotations

import concurrent
import math
from typing import List, TYPE_CHECKING

from evonote import EvolverInstance
from evonote.file_helper.evolver import save_cache

if TYPE_CHECKING:
    from evonote.core.neuron import Neuron
    from evonote.core.note import Note
from evonote.model.llm import get_embeddings, cache_embeddings, complete_chat

import numpy as np

class VectorIndex:
    def __init__(self, vecs, items):
        self.vecs = vecs
        self.items = items


class KnowledgeItem:
    def __init__(self):
        # attention vectors for calculating similarity
        # it contains a list of attention vectors
        #  from related notes can also be added
        self._attention_vector = None
        self._attention_bias = None
        self._attention_src = []
        self._is_root = False

        self._vector_index: VectorIndex | None = None

    def index_descendants(self):
        attention_vec_list = []
        src_list = []
        children_index_start = []
        children = self.get_descendants()
        children_non_empty = []
        for child in children:
            if len(child._attention_src) == 0:
                continue
            children_non_empty.append(child)
            children_index_start.append(len(src_list))
            src_list.extend(child._attention_src)
        src_embedding_list = get_embeddings(src_list)

        for i, start_index in enumerate(children_index_start[:-1]):
            child_embedding_list = src_embedding_list[start_index: start_index + len(children_non_empty[i]._attention_src)]
            attention_vec_list.append(np.sum(child_embedding_list, axis=0) / (len(child_embedding_list)**0.7))

        self._vector_index = VectorIndex(np.array(attention_vec_list), children_non_empty)
        cache_embeddings()

    def get_similar_descendents(self, texts: List[str], weights: List[float] = None):
        text_embedding_list = get_embeddings(texts)
        if self._vector_index is None:
            self.index_descendants()
        text_embedding_list = np.array(text_embedding_list)
        similarity = self._vector_index.vecs.dot(text_embedding_list.T).T

        if weights is None:
            similarity = np.sum(similarity, axis=0)
        else:
            similarity = np.sum(similarity * np.array(weights), axis=0)

        rank = np.argsort(similarity, axis=0)[::-1]
        top_30 = rank[:30]
        top_30 = top_30.T
        children = self._vector_index.items
        top_30_children = []
        for i in top_30:
            print(i)
            top_30_children.append(children[i])

        return top_30_children

    def get_similarity(self, vecs: np.ndarray):
        if self._vector_index is None:
            self.index_descendants()
        return self._vector_index.vecs.dot(vecs.T)

    def get_descendants(self):
        raise NotImplementedError()


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
    chat = Chat(user_message="Split the following sentence into smaller fragments (no more than about 8 words). Put each fragment in a new line.",
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

def make_frag_indexing(note: Note, use_cache=True, caller_path=None):
    if caller_path is None:
        _, _, stack = EvolverInstance.get_context()
        caller_path = stack[0].filename

    break_sent_use_cache = lambda sent: break_sent_into_frags(sent, use_cache, caller_path)

    children = note.get_descendants()
    children_content = []
    children_non_empty = []


    for child in children:
        if len(child._content) == 0:
            continue
        children_content.append(child._content)
        children_non_empty.append(child)
    n_finished = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        for child, frags in zip(children_non_empty, executor.map(break_sent_use_cache, children_content)):
            child._attention_src.extend(frags)
            keywords_on_path = child._note_path.split('/')[1:]
            if len(keywords_on_path) != 0:
                # keep last 1/3 of the keywords
                n_keywords = math.ceil(len(keywords_on_path) / 3)
                child._attention_src.extend(keywords_on_path[-n_keywords:])
            child._attention_src.append(child._content)
            #print(child._attention_src)
            n_finished += 1
            if n_finished % 20 == 19:
                save_cache()
    save_cache()

'''
class RootKnowledgeItem(KnowledgeItem):
    def __init__(self):
        super().__init__()
        self._is_root = True

    def get_items(self):
        raise NotImplementedError()


class KnowledgeBase:
    def __init__(self):
        #self.root_items: List[KnowledgeItem] = []
        #self.notes: List[Note] = []
        self.neurons: List[Neuron] = []

        self.neuron_attention_vecs: np.ndarray | None = None
        self.neuron_attention_index = []

        self.neuron_target_vecs: np.ndarray | None = None
        self.neuron_target_index = []

    def add_neurons(self, neurons: List[Neuron]):
        self.neurons.extend(neurons)

    def index_items(self):
        src_list = []
        attention_index_start = []
        for neuron in self.neurons:
            for src in neuron._attention_src:
                attention_index_start.append(len(src_list))
                src_list.extend(src)

        attention_vec_list = get_embeddings(src_list)

        self.neuron_attention_vecs = np.array(attention_vec_list)
        self.neuron_attention_index = attention_index_start



        src_list = []
        target_index_start = []
        for neuron in self.neurons:
            target_index_start.append(len(neuron._target_src))
            for src in neuron._target_src:
                src_list.extend(src)

        target_vec_list = get_embeddings(src_list)

        self.neuron_target_vecs = np.zeros(len(target_vec_list))
        #self.neuron_target_index = target_index_start

        cache_embeddings()




    def search_notes(self, key_words: List[str], notes: List[Note]):
        kw_vecs = get_embeddings(key_words)

    def evolve_neurons(self, target_vecs: np.ndarray):

        if not isinstance(target_vecs, np.ndarray):
            target_vecs = np.array(target_vecs)

        attention_index = self.neuron_attention_index
        attention_vecs: np.ndarray = self.neuron_attention_vecs

        input_excitation = attention_vecs.dot(target_vecs.T)

        # Pass input into a ReLU
        input_excitation = np.maximum(input_excitation, 0)

        sum_of_excitation = []
        coeffs = np.zeros(len(attention_index))
        i = 0
        for neuron in self.neurons:
            for j, src in enumerate(neuron._attention_src):
                vec_index_end = attention_index[i] + len(src)
                excitation = input_excitation[attention_index[i]: vec_index_end]
                sum_of_excitation.append(np.sum(excitation, axis=0)[0] / len(src))
                coeffs[i] = neuron._attention_bias[j]
                i += 1

        before_excitation = 10 * (np.array(sum_of_excitation) + coeffs)
        after_excitation = 1 / (1 + np.exp(-before_excitation))

        max_excitations = []
        i = 0
        for neuron in self.neurons:
            excitation = after_excitation[i:i+len(neuron._attention_src)]
            i += len(neuron._attention_src)

            # Select the largest excitation
            max_excitations.append(np.max(excitation))

        max_excitations = np.array(max_excitations)

        output_excitations = 1 / (1 +  np.exp(-10 *(max_excitations - 0.7)))

        top_k = 2
        # Select the neurons with top_k excitation
        triggered_neuron_indices = np.argsort(output_excitations)[-top_k:][::-1]
        triggered_neurons = [self.neurons[i] for i in triggered_neuron_indices]
        triggered_srcs = [src for neuron in triggered_neurons for src in neuron._target_src]

        return
        #new_target_vecs =


if __name__ == "__main__":
    from evonote.core.neuron import Neuron
    knowledge_base = KnowledgeBase()

    n1 = Neuron(["hello"], ["world"])
    n2 = Neuron(["hello", "world"], ["hello world"])
    n3 = Neuron(["hello world"], ["new to programming"])
    n4 = Neuron(["John", "Matthew"], ["Man"])

    neurons = [n1, n2, n3, n4]

    knowledge_base.add_neurons(neurons)

    knowledge_base.index_items()

    vecs = get_embeddings(["Mike"], make_cache=True)

    knowledge_base.evolve_neurons(vecs)
    
'''
