import evonote
from evonote.debug import display_chats, display_embedding_search
from evonote.indexing.code_indexer import CodeDocsIndexer
from evonote.indexing.core import FragmentedEmbeddingIndexer, \
    IndexingSearchLogger
from evonote.search.code_searcher import search_function
from evonote.testing import v_lab
from evonote.builder.extract_from_module import get_notebook_for_module


notebook = get_notebook_for_module(v_lab)
notebook.make_indexing(CodeDocsIndexer)
#notebook.show_notebook_gui()
with display_embedding_search():
    with display_chats():
        notebook = search_function("Add water", notebook)
        notebook.show_notebook_gui()