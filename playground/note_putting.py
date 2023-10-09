from evonote.notetree import Note
from evonote.notetree import Tree
from evonote.transform.note_putting import add_content_to_notetree


memory_notetree = Tree("memory of things",
                           rule_of_path="Example: \"Bob's birthday is in October\""
                                        " is stored in path /People/Bob/birthday ")

sample_note = Note(memory_notetree).be("Charles's birthday is in October")
memory_notetree.add_note_by_path(["People", "Charles", "birthday"], sample_note)

add_content_to_notetree("Alice died in April", "", memory_notetree)
add_content_to_notetree("Canada is in America", "", memory_notetree)

memory_notetree.show_notetree_gui()
