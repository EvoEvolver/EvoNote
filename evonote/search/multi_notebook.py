from typing import List

from evonote.core.notebook import Notebook
from evonote.search.fine_searcher import filter_notebook_in_group


def search_related_notebook_to_store(content_to_store, bookshelf: Notebook,
                                     use_cache=True) -> List[Notebook]:
    criteria_prompt = ("Whether the note describes a notebook "
                       "that is suitable for storing the following content:")
    criteria_prompt += f"\n{content_to_store}"
    sub_bookshelf = filter_notebook_in_group(bookshelf, criteria_prompt,
                                             use_cache=use_cache)
    res = []
    for note in sub_bookshelf.children:
        if note.resource.has_type("notebook"):
            notebook = note.resource.get_resource_by_type("notebook")
            res.append(notebook)
    return res
