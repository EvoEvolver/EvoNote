from evonote.mindtree import Tree


class AgentState:
    def __init__(self):
        self.root_tree = Tree(
            "root tree that indexes all available trees")
        self.objective_stack = []
        self.logs = []
