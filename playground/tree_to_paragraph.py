import os

from evonote import debug
from evonote.transform.build_from_sections import digest_all_descendants
from evonote.transform.tree_to_paragraph import tree_to_paragraph
from evonote.mindtree import Tree


with debug.display_chats():
    os.system("python gen_sample_paper_tree.py")
    tree = Tree.load("AI4Science.enb")
    keyword = "quantum computing"
    tree = tree.get_sub_tree_by_similarity([keyword], top_k=6)
    res = tree_to_paragraph(tree,
                                f"You should focus on writing about {keyword}")
    print(res)
    new_tree = Tree()
    note = new_tree.get_new_note_by_path([keyword])
    note.be(res)
    new_tree = digest_all_descendants(new_tree)
    new_tree.show_tree_gui()
