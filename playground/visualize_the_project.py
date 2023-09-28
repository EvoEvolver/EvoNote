import evonote
from evonote.transform.module_to_notebook import get_notebook_for_module

notebook = get_notebook_for_module(evonote)
notebook.show_notebook_gui()