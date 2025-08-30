from collections import dequeu

## need node class to track state, pointer to parent, action, path cost, and depth
class Node:

    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.depth = 0
        if parent:
            self.depth += parent.depth
        
    def __str__(self):
        return f'Node {self.state}'
    
    def next_nodes(self):
        pass