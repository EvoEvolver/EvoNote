from evonote.mindtree import Tree

tree = Tree.load("AI4Science.enb")

keyword = "quantum computing"

tree = tree.get_sub_tree_by_similarity([keyword], top_k=10)

tree.show_tree_gui()