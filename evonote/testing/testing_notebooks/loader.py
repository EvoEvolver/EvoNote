import os

from evonote.data_cleaning.document import Document
from evonote.notebook.notebook import Notebook
from evonote.transform.build_from_sections import notebook_from_doc

curr_dir = os.path.dirname(os.path.abspath(__file__))


def load_sample_notebook(path: str) -> Notebook:
    """
    Args:
        path: The relative path to the json file.

    Returns:
        The notebook loaded from the json file.
    """
    if not path.endswith(".json"):
        path += ".json"
    doc = Document.from_json(os.path.join(curr_dir, path))
    notebook = notebook_from_doc(doc, {'title': doc.title})
    return notebook
