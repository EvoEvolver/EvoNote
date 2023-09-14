from evonote.notebook.notebook import Notebook

notebook = Notebook.load("AI4Science.enb")

keyword = "quantum computing"

notebook = notebook.get_sub_notebook_by_similarity([keyword], top_k=10)

notebook.show_notebook_gui()