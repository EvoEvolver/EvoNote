from __future__ import annotations
from typing import List

from evonote.model.llm import get_embeddings, cache_embeddings
import numpy as np


class VectorIndexer:
    @classmethod
    def get_vectors(cls, indices: List[VectorIndexer]):
        """
        Calculate the vectors in batch
        """
        raise NotImplementedError

    @classmethod
    def get_similarities(cls, texts: List[str], vecs: np.ndarray, weights: List[float] = None):
        raise NotImplementedError

class EmbedIndexer(VectorIndexer):
    def __init__(self):
        self.src_list: List[str] = []
        self.src_weights: List[float] = []

    def extend_src(self, src_list: List[str], src_weights: List[float] = None):
        self.src_list.extend(src_list)
        if src_weights is None:
            src_weights = [1.0] * len(src_list)
        self.src_weights.extend(src_weights)

    def add_src(self, src: str, weight: float = 1.0):
        self.src_list.append(src)
        self.src_weights.append(weight)

    @classmethod
    def get_vectors(cls, indices: List[EmbedIndexer]):
        vec_list = []
        src_list = []
        children_index_start = []
        for child in indices:
            if len(child.src_list) == 0:
                children_index_start.append(-1)
                continue
            children_index_start.append(len(src_list))
            src_list.extend(child.src_list)

        src_embedding_list = get_embeddings(src_list)

        embedding_dim = len(src_embedding_list[0])

        for i, start_index in enumerate(children_index_start[:-1]):
            if start_index == -1:
                vec_list.append(np.zeros(embedding_dim))
                continue
            child_embedding_list = src_embedding_list[start_index: start_index + len(
                indices[i].src_list)]
            vec_list.append(
                np.sum(child_embedding_list, axis=0) / (len(child_embedding_list) ** 0.8))

        cache_embeddings()

        return np.array(vec_list)

    @classmethod
    def get_similarities(cls, texts: List[str], vecs: np.ndarray, weights: List[float] = None):
        text_embedding_list = get_embeddings(texts)
        text_embedding_list = np.array(text_embedding_list)
        similarity = vecs.dot(text_embedding_list.T).T

        if weights is None:
            weights = [1.0]*len(vecs)

        similarity = np.sum(similarity * np.array(weights), axis=0)
        return similarity

