from evonote.file_helper.cache_manage import save_used_cache, save_cache
from evonote.transform.build_from_sections import digest_all_descendants, \
    mindtree_from_doc
from evonote.data_cleaning.html_converter import process_html_into_standard

from evonote.testing.sample_html import sample_html
# html = open("./ListenbourgWiki.html", "r", encoding="utf-8").read()

doc, meta = process_html_into_standard(sample_html)

paper_tree = mindtree_from_doc(doc, meta)

digest_tree = digest_all_descendants(paper_tree)

# Try removing comments to show the tree before digesting

# paper_tree.show_tree_gui()

digest_tree.show_tree_gui()

save_used_cache()

# Try removing comments to save the tree

# digest_tree.save("AI4Science.enb")