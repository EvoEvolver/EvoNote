from evonote.notebook.notebook import Notebook
from evonote.testing.testing_notebooks.loader import load_sample_notebook


def test_adding_and_parent():
    notebook = Notebook("test")
    note1 = notebook.get_new_note_by_path(["a", "b", "c"]).be("test1")
    note2 = notebook.add_note_by_path(["a", "b", "d"], "test2")
    note3 = notebook.get_note_by_path(["a", "b"]).be("test3")
    assert note1.parent().content == "test3" == note3.content == note2.parent().content


def test_adding_twice():
    notebook = Notebook("test")
    notebook.get_new_note_by_path(["a", "b", "c"]).be("test1")
    notebook.add_note_by_path(["a", "b", "c"], "test2")
    assert notebook.get_note_by_path(["a", "b", "c"]).content == "test2"


def test_notebook_copy():
    notebook = load_sample_notebook("dingzhen_world.json")
    notebook2 = notebook.duplicate_notebook_by_note_mapping(lambda note, new_notebook: note)
    assert notebook2.get_dict_for_prompt() == notebook.get_dict_for_prompt()