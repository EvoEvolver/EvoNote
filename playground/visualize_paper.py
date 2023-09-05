from evonote.writer.build_from_sections import digest_all_descendants, \
    notebook_from_doc
from evonote.data_cleaning.latex import process_latex_into_standard


tex = open("AI4Science.tex", "r", encoding="utf-8").read()

doc, meta = process_latex_into_standard(tex)

paper_notebook = notebook_from_doc(doc, meta)

digest_all_descendants(paper_notebook)

paper_notebook.show_notebook_gui()