from evonote.notebook.notebook import Notebook

dingzhen_world = Notebook("An introduction to the republic of Ganzi")

dingzhen_world.get_new_note_by_path(["Ganzi"]).be(
    "The republic of Ganzi is a country in the world.")
dingzhen_world.get_new_note_by_path(["Ganzi", "Capital"]).be(
    "Litang is the capital of the republic of Ganzi.")
dingzhen_world.get_new_note_by_path(["Ganzi", "Leaders"]).be(
    "There are many leaders in of the republic of Ganzi.")
dingzhen_world.get_new_note_by_path(["Ganzi", "Leaders", "President"]).be(
    "Dingzhen is the president of the republic of Ganzi.")
dingzhen_world.get_new_note_by_path(["Ganzi", "Leaders", "Vice President"]).be(
    "Ruike is the vice president of the republic of Ganzi.")
dingzhen_world.get_new_note_by_path(["Dingzhen", "Pet"]).be(
    "Zhenzhu the horse is the pet of the president of the republic of Ganzi.")
dingzhen_world.get_new_note_by_path(["Dingzhen", "Motto"]).be(
    "It's the mother who give me life.")
