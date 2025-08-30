from collections import dequeu

## need node class to track state, pointer to parent, action, path cost, and depth
class Node:

    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        
    def __str__(self):
        return f'Node {self.state}'
    