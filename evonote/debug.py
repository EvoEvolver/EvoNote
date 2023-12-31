from evonote.file_helper.cache_manage import cache_manager
from evonote.indexing.core import IndexingSearchLogger
from evonote.model.chat import ChatLogger
from evonote.utils import debugger_is_active

is_debug = debugger_is_active()

def display_chats():
    return ChatLogger()


def display_embedding_search():
    return IndexingSearchLogger()


def refresh_cache():
    return cache_manager.refresh_cache()
