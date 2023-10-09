from evonote.file_helper.cache_manage import save_used_cache, save_cache
from evonote.testing.sample_paper import sample_paper
from evonote.transform.build_from_sections import digest_all_descendants, \
    notetree_from_doc
from evonote.data_cleaning.latex_converter import process_latex_into_standard


tex = sample_paper

doc, meta = process_latex_into_standard(tex)

paper_notetree = notetree_from_doc(doc, meta)

digest_notetree = digest_all_descendants(paper_notetree)

# Try removing comments to show the notetree before digesting

# paper_notetree.show_notetree_gui()

digest_notetree.show_notetree_gui()

save_used_cache()

# Try removing comments to save the notetree

digest_notetree.save("AI4Science.enb")