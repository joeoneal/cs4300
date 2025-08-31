from collections import deque
from domains.wgc import WGC
## need node class to track state, pointer to parent, action, path cost, and depth
class Node:

    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        
    def __str__(self):
        return f'Node {self.state}'
    
#############################################################################

def main(): 

    problem = WGC()
    start = Node(problem.init_state, None)
    frontier = deque()
    frontier.append(start)
    explored = set()
    
    print(f'First node in the queue is {start}.')
    print(f'goal state is {problem.goal_state}')

    while frontier:
        node_being_tested = frontier.popleft()
        print(f'goal testing {node_being_tested}...')

        if problem.goal_test(node_being_tested.state):
            print(f'Solution found: {node_being_tested.state}')
            return
        explored.add(node_being_tested.state)
        for action in problem.possibleActions(node_being_tested.state):
            new_state = problem.result(node_being_tested.state, action)
            if new_state not in explored:
                new_node = Node(new_state, node_being_tested)
                frontier.append(new_node)

    print("search failed")
    return


