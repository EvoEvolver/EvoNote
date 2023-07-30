from typing import Tuple, List

from evonote.core.knowledge import KnowledgeItem, RootKnowledgeItem


class NeuralNetwork(RootKnowledgeItem):
    def __init__(self):
        super().__init__()
        self._neurons = []
        self._is_neuron = True

    def get_items(self):
        pass

class Neuron(KnowledgeItem):
    def __init__(self, attentions: List | None=None, targets: List |None=None):
        super().__init__()
        self._is_neuron = True
        self._target_vectors = []
        self._target_src: List[Tuple[str]] = []
        self._label = None
        if attentions is not None:
            for src in attentions:
                self.add_attention_src(src)
        if targets is not None:
            for src in targets:
                self.add_target_src(src)

    def add_target_src(self, src: List[str] | str):
        if isinstance(src, str):
            src = (src,)
        self._target_src.append(src)