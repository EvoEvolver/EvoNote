from evonote.file_helper.cache_manage import save_used_cache, save_cache
from evonote.transform.build_from_sections import digest_all_descendants, \
    notebook_from_doc
from evonote.data_cleaning.latex_converter import process_latex_into_standard


tex = open("AI4Science.tex", "r", encoding="utf-8").read()

doc, meta = process_latex_into_standard(tex)

paper_notebook = notebook_from_doc(doc, meta)

digest_notebook = digest_all_descendants(paper_notebook)

# Try removing comments to show the notebook before digesting

# paper_notebook.show_notebook_gui()

digest_notebook.show_notebook_gui()

save_used_cache()

# Try removing comments to save the notebook

# digest_notebook.save("AI4Science.enb")