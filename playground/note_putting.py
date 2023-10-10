from evonote.mindtree import Note
from evonote.mindtree import Tree
from evonote.transform.note_putting import add_content_to_tree


memory_tree = Tree("memory of things",
                           rule_of_path="Example: \"Bob's birthday is in October\""
                                        " is stored in path /People/Bob/birthday ")

sample_note = Note(memory_tree).be("Charles's birthday is in October")
memory_tree.add_note_by_path(["People", "Charles", "birthday"], sample_note)

add_content_to_tree("Alice died in April", "", memory_tree)
add_content_to_tree("Canada is in America", "", memory_tree)

memory_tree.show_tree_gui()
