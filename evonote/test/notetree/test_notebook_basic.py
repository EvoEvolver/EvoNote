from evonote.mindtree import Tree
from evonote.testing.testing_trees.loader import load_sample_tree


def test_adding_and_parent():
    tree = Tree("test")
    note1 = tree.get_new_note_by_path(["a", "b", "c"]).be("test1")
    note2 = tree.add_note_by_path(["a", "b", "d"], "test2")
    note3 = tree.get_note_by_path(["a", "b"]).be("test3")
    assert note1.parent().content == "test3" == note3.content == note2.parent().content


def test_adding_twice():
    tree = Tree("test")
    tree.get_new_note_by_path(["a", "b", "c"]).be("test1")
    tree.add_note_by_path(["a", "b", "c"], "test2")
    assert tree.get_note_by_path(["a", "b", "c"]).content == "test2"


def test_tree_copy():
    tree = load_sample_tree("dingzhen_world.json")
    tree2 = tree.duplicate_tree_by_note_mapping(lambda note, new_tree: note)
    assert tree2.get_dict_for_prompt() == tree.get_dict_for_prompt()