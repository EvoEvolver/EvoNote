import evonote
from evonote.transform.extract_from_module import get_notebook_for_module

notebook = get_notebook_for_module(evonote)
notebook.show_notebook_gui()