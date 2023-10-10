from evonote.file_helper.cache_manage import save_used_cache, save_cache
from evonote.testing.sample_paper import sample_paper
from evonote.transform.build_from_sections import digest_all_descendants, \
    mindtree_from_doc
from evonote.data_cleaning.latex_converter import process_latex_into_standard


tex = sample_paper

doc, meta = process_latex_into_standard(tex)

paper_tree = mindtree_from_doc(doc, meta)

digest_tree = digest_all_descendants(paper_tree)

# Try removing comments to show the tree before digesting

# paper_tree.show_tree_gui()

digest_tree.show_tree_gui()

save_used_cache()

# Try removing comments to save the tree

digest_tree.save("AI4Science.enb")