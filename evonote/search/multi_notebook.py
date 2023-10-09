from typing import List

from evonote.notetree import Tree
from evonote.search.fine_searcher import filter_notetree_in_group


def search_related_notetree_to_store(content_to_store, bookshelf: Tree) -> List[
    Tree]:
    criteria_prompt = ("Whether the note describes a notetree "
                       "that is suitable for storing the following content:")
    criteria_prompt += f"\n{content_to_store}"
    sub_bookshelf = filter_notetree_in_group(bookshelf, criteria_prompt)
    res = []
    for note in sub_bookshelf.children:
        if note.resource.has_type("notetree"):
            notetree = note.resource.get_resource_by_type("notetree")
            res.append(notetree)
    return res
