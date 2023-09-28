from evonote.file_helper.cache_manage import save_used_cache, save_cache
from evonote.transform.build_from_sections import digest_all_descendants, \
    notebook_from_doc
from evonote.data_cleaning.html_converter import process_html_into_standard

from evonote.testing.sample_html import sample_html
# html = open("./ListenbourgWiki.html", "r", encoding="utf-8").read()

doc, meta = process_html_into_standard(sample_html)

paper_notebook = notebook_from_doc(doc, meta)

digest_notebook = digest_all_descendants(paper_notebook)

# Try removing comments to show the notebook before digesting

# paper_notebook.show_notebook_gui()

digest_notebook.show_notebook_gui()

save_used_cache()

# Try removing comments to save the notebook

# digest_notebook.save("AI4Science.enb")