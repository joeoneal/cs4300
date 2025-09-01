from collections import deque
from domains.wgc import WGC
## need node class to track state, pointer to parent, action, path cost, and depth
class Node:

    def __init__(self, state, parent=None, action = None):
        self.state = state
        self.parent = parent
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1
        self.total = 1
        self.action = action

    def __str__(self):
        return f'Node {self.state}'
    
#############################################################################

def bfs(): 

    problem = WGC()
    start = Node(problem.init_state, None)
    problem.total_nodes += 1
    frontier = deque()
    frontier.append(start)
    explored = set()
    
    # print(f'First node in the queue is {start}.')
    # print(f'goal state is {problem.goal_state}')

    while frontier:
        # print(f"frontier length is {len(frontier)}")
        node_being_tested = frontier.popleft()
        # print(f'goal testing {node_being_tested}...')

        if problem.goal_test(node_being_tested.state):
            # print(f'Solution found: {node_being_tested.state}')
            # print(f'steps taken: {node_being_tested.depth}')
            return (node_being_tested, problem.total_nodes, problem.nodes_expanded, problem.max_frontier)
        
        # need flag to check for child nodes
        has_child = False
        explored.add(node_being_tested.state)
        for action in problem.possibleActions(node_being_tested.state):
            if not has_child:
                problem.nodes_expanded += 1
                has_child = True

            new_state = problem.result(node_being_tested.state, action)
            if new_state not in explored:
                new_node = Node(new_state, node_being_tested, action)
                problem.total_nodes += 1

                frontier.append(new_node)
                if problem.max_frontier < len(frontier):
                    problem.max_frontier = len(frontier)

    print("search failed")
    return None


