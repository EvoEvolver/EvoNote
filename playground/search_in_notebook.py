from evonote.notetree import Tree

notetree = Tree.load("AI4Science.enb")

keyword = "quantum computing"

notetree = notetree.get_sub_notetree_by_similarity([keyword], top_k=10)

notetree.show_notetree_gui()