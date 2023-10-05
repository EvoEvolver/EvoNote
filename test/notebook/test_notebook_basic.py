from evonote.notebook.notebook import Notebook


def test_adding_and_parent():
    notebook = Notebook("test")
    note1 = notebook.get_new_note_by_path(["a", "b", "c"]).be("test1")
    note2 = notebook.add_note_by_path(["a", "b", "d"], "test2")
    note3 = notebook.get_note_by_path(["a", "b"]).be("test3")
    a = note2.get_parent()
    assert note1.get_parent().content == "test3" == note3.content == note2.get_parent().content