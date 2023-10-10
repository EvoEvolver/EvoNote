from typing import List

from evonote.mindtree import Tree
from evonote.search.fine_searcher import filter_tree_in_group


def search_related_tree_to_store(content_to_store, bookshelf: Tree) -> List[
    Tree]:
    criteria_prompt = ("Whether the note describes a tree "
                       "that is suitable for storing the following content:")
    criteria_prompt += f"\n{content_to_store}"
    sub_bookshelf = filter_tree_in_group(bookshelf, criteria_prompt)
    res = []
    for note in sub_bookshelf.children:
        if note.resource.has_type("tree"):
            tree = note.resource.get_resource_by_type("tree")
            res.append(tree)
    return res
