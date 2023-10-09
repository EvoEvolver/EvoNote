from evonote.notetree import Tree


class AgentState:
    def __init__(self):
        self.root_notetree = Tree(
            "root notetree that indexes all available notetrees")
        self.objective_stack = []
        self.logs = []
