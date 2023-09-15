from evonote import debug
from evonote.transform.build_from_sections import digest_all_descendants
from evonote.transform.notebook_to_paragraph import notebook_to_paragraph
from evonote.notebook.notebook import Notebook


with debug.display_chats():
    notebook = Notebook.load("AI4Science.enb")
    keyword = "quantum computing"
    notebook = notebook.get_sub_notebook_by_similarity([keyword], top_k=6)
    res = notebook_to_paragraph(notebook,
                                f"You should focus on writing about {keyword}")
    new_notebook = Notebook(keyword)
    note = new_notebook.get_new_note_by_path([keyword])
    note.be(res)
    new_notebook = digest_all_descendants(new_notebook)
    new_notebook.show_notebook_gui()
