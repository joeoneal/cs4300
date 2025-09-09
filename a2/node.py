class Node:
    def __init__(self, state, parent = None, action = None):
        self.state = state
        self.parent = parent
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1
        self.action = action

    def __str__(self):
        return f'Node {self.state}'