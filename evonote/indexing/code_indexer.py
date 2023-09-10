from typing import List

from evonote.builder.extract_from_module import FunctionDocs
from evonote.indexing.core import AbsEmbeddingIndexer, Indexing
from evonote.notebook.note import Note


class CodeParameterIndexer(AbsEmbeddingIndexer):
    @classmethod
    def prepare_src_weight_list(cls, new_notes: List[Note], indexing: Indexing,
                                ) -> (
            List[List[str]], List[List[float]], List[Note]):
        note_can_index = []
        contents = []
        weight_list = []
        for note in new_notes:
            docs: FunctionDocs
            function, docs = note.resource.get_resource_and_docs_by_type("function")
            if docs is not None and len(docs.params) > 0:
                function_name = underscore_to_space(function.__name__)
                for param_name, param_doc in docs.params.items():
                    param_name = underscore_to_space(param_name)
                    contents.append([param_name, function_name, param_doc])
                    weight_list.append([0.4, 0.1, 0.5])
                    note_can_index.append(note)
        return contents, weight_list, note_can_index


class CodeReturnIndexer(AbsEmbeddingIndexer):
    @classmethod
    def prepare_src_weight_list(cls, new_notes: List[Note], indexing: Indexing,
                                ) -> (
            List[List[str]], List[List[float]], List[Note]):
        note_can_index = []
        contents = []
        weight_list = []
        for note in new_notes:
            docs: FunctionDocs
            function, docs = note.resource.get_resource_and_docs_by_type("function")
            if docs is not None and len(docs.returns) > 0:
                if function.__annotations__["return"] is None:
                    continue
                contents_for_note = []
                weights_for_note = []
                function_name = underscore_to_space(function.__name__)
                note_can_index.append(note)
                contents_for_note.append(function_name)
                weights_for_note.append(1.0)
                if len(docs.general) > 0:
                    contents_for_note.append(docs.general)
                    weights_for_note.append(1.0)
                if len(docs.returns) > 0:
                    contents_for_note.append(docs.returns)
                    weights_for_note.append(2.0)
                contents.append(contents_for_note)
                weight_sum = sum(weights_for_note)
                weights_for_note = [w / weight_sum for w in weights_for_note]
                weight_list.append(weights_for_note)
        return contents, weight_list, note_can_index


class CodeDocsIndexer(AbsEmbeddingIndexer):
    @classmethod
    def prepare_src_weight_list(cls, new_notes: List[Note], indexing: Indexing,
                                ) -> (
            List[List[str]], List[List[float]], List[Note]):
        note_can_index = []
        contents = []
        weight_list = []
        for note in new_notes:
            docs: FunctionDocs
            function, docs = note.resource.get_resource_and_docs_by_type("function")
            if docs is not None:
                function_name = underscore_to_space(function.__name__)
                note_can_index.append(note)
                contents.append([function_name])
                weight_list.append([1.0])
                print(function_name)
                if len(docs.general) > 0:
                    note_can_index.append(note)
                    contents.append([docs.general, function_name])
                    weight_list.append([0.7, 0.3])
                # for keyword in docs.keywords:
                #    note_can_index.append(note)
                #    contents.append([keyword, function_name])
                #    weight_list.append([0.6, 0.4])
        return contents, weight_list, note_can_index


def underscore_to_space(s: str):
    return s.replace("_", " ")
