from evonote.notebook.notebook import Notebook

class AgentState:
    def __init__(self):
        self.root_notebook = Notebook("root notebook that indexes all available notebooks")
        self.objective_stack = []
        self.logs = []