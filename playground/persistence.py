import os

from evonote.mindtree import Tree

os.system("python gen_sample_paper_tree.py")
tree = Tree.load("AI4Science.enb")

tree.show_tree_gui()