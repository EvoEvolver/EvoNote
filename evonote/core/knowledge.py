from __future__ import annotations
from typing import List, TYPE_CHECKING
if TYPE_CHECKING:
    from evonote.core.neuron import Neuron
    from evonote.core.note import Note
from evonote.model.llm import get_embeddings, cache_embeddings

import numpy as np

class KnowledgeItem:
    def __init__(self):
        # attention vectors for calculating similarity
        # it contains a list of attention vectors
        # vectors from related notes can also be added
        self._attention_vectors = []
        self._attention_bias = []
        self._attention_src = []
        self._is_root = False
        
    def add_attention_src(self, src: List[str] | str):
        if isinstance(src, str):
            src = (src,)
        self._attention_src.append(src)
        self._attention_bias.append(-0.7)

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
