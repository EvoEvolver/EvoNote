from evonote import debug
from evonote.transform.build_from_sections import digest_all_descendants
from evonote.transform.notetree_to_paragraph import notetree_to_paragraph
from evonote.notetree import Tree


with debug.display_chats():
    notetree = Tree.load("AI4Science.enb")
    keyword = "quantum computing"
    notetree = notetree.get_sub_notetree_by_similarity([keyword], top_k=6)
    res = notetree_to_paragraph(notetree,
                                f"You should focus on writing about {keyword}")

    # Refactor the notetree

    new_notetree = Tree(keyword)
    note = new_notetree.get_new_note_by_path([keyword])
    note.be(res)
    new_notetree = digest_all_descendants(new_notetree)
    new_notetree.show_notetree_gui()
