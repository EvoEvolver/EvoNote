from evonote.mindtree import Tree


def analyze_tree_sparsity(tree: Tree):
    """
    Return the average number of children per note.
    """
    notes = tree.get_note_list()
    max_children = -1
    total_children = 0
    n_non_leaf_notes = 0
    for note in notes:
        n_children = len(note.children())
        if n_children > 0:
            n_non_leaf_notes += 1
            total_children += n_children
        max_children = max(max_children, n_children)
    average_children = total_children / n_non_leaf_notes
    heavy_notes = get_children_heavy_notes(tree)
    print("Total_notes:", len(notes))
    print("Average children per non-leaf note:", average_children)
    print("Max children per note:", max_children)
    # print heavy notes
    for note in heavy_notes:
        print("Note:", note.note_path())
        print("Children:", len(note.children()))
        print("Content:", note.content)
        print("")

def get_children_heavy_notes(tree: Tree, min_children=8):
    """
    Return a list of notes with at least min_children children.
    """
    notes = tree.get_note_list()
    heavy_notes = []
    for note in notes:
        n_children = len(note.children())
        if n_children >= min_children:
            heavy_notes.append(note)
    return heavy_notes