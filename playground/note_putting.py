from evonote.core.note import Note
from evonote.core.notebook import Notebook
from evonote.writer.note_putting import add_content_to_notebook


memory_notebook = Notebook("memory of things",
                           rule_of_path="Example: \"Bob's birthday is in October\""
                                        " is stored in path /People/Bob/birthday ")

memory_notebook.add_note_by_path(["People", "Bob", "birthday"], Note(
    memory_notebook).be("Bob's birthday is in October"))

add_content_to_notebook("Alice died in April", "", memory_notebook)
add_content_to_notebook("Canada is in America", "", memory_notebook)

memory_notebook.show_notebook_gui()
