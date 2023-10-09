from evonote.file_helper.cache_manage import save_used_cache, save_cache
from evonote.transform.build_from_sections import digest_all_descendants, \
    notetree_from_doc
from evonote.data_cleaning.html_converter import process_html_into_standard

from evonote.testing.sample_html import sample_html
# html = open("./ListenbourgWiki.html", "r", encoding="utf-8").read()

doc, meta = process_html_into_standard(sample_html)

paper_notetree = notetree_from_doc(doc, meta)

digest_notetree = digest_all_descendants(paper_notetree)

# Try removing comments to show the notetree before digesting

# paper_notetree.show_notetree_gui()

digest_notetree.show_notetree_gui()

save_used_cache()

# Try removing comments to save the notetree

# digest_notetree.save("AI4Science.enb")