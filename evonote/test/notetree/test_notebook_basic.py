from evonote.notetree import Tree
from evonote.testing.testing_trees.loader import load_sample_notetree


def test_adding_and_parent():
    notetree = Tree("test")
    note1 = notetree.get_new_note_by_path(["a", "b", "c"]).be("test1")
    note2 = notetree.add_note_by_path(["a", "b", "d"], "test2")
    note3 = notetree.get_note_by_path(["a", "b"]).be("test3")
    assert note1.parent().content == "test3" == note3.content == note2.parent().content


def test_adding_twice():
    notetree = Tree("test")
    notetree.get_new_note_by_path(["a", "b", "c"]).be("test1")
    notetree.add_note_by_path(["a", "b", "c"], "test2")
    assert notetree.get_note_by_path(["a", "b", "c"]).content == "test2"


def test_notetree_copy():
    notetree = load_sample_notetree("dingzhen_world.json")
    notetree2 = notetree.duplicate_notetree_by_note_mapping(lambda note, new_notetree: note)
    assert notetree2.get_dict_for_prompt() == notetree.get_dict_for_prompt()