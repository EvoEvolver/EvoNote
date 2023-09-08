from evonote.core.note import Note
from evonote.core.notebook import Notebook
from evonote.writer.note_putting import add_content_to_notebook


memory_notebook = Notebook("memory of things",
                           rule_of_path="Example: \"Bob's birthday is in October\""
                                        " is stored in path /People/Bob/birthday ")

sample_note = Note(memory_notebook).be("Charles's birthday is in October")
memory_notebook.add_note_by_path(["People", "Charles", "birthday"], sample_note)

add_content_to_notebook("Alice died in April", "", memory_notebook)
add_content_to_notebook("Canada is in America", "", memory_notebook)

memory_notebook.show_notebook_gui()
