import os

from evonote.data_cleaning.document import Document
from evonote.notetree import Tree
from evonote.transform.build_from_sections import notetree_from_doc

curr_dir = os.path.dirname(os.path.abspath(__file__))


def load_sample_notetree(path: str) -> Tree:
    """
    Args:
        path: The relative path to the json file.

    Returns:
        The notetree loaded from the json file.
    """
    if not path.endswith(".json"):
        path += ".json"
    doc = Document.from_json(os.path.join(curr_dir, path))
    notetree = notetree_from_doc(doc, {'title': doc.title})
    return notetree
