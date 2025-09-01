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
    
################################################################################################

def bfs(problem): 

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

###################################################################################################################

# need dls function first
def dls(problem, L):
    start = Node(problem.init_state, None)
    frontier = []
    frontier.append(start)
    cutoff = False

    #keep track of stats locally in this one
    stats = {"total": 1, "expanded": 0, "max_frontier": 1}

    while frontier:
        node_being_tested = frontier.pop()
        if problem.goal_test(node_being_tested.state):
            return (node_being_tested, stats["total"], stats["expanded"], stats["max_frontier"])
        
        if node_being_tested.depth == L:
            cutoff = True
            continue
        
        actions = problem.possibleActions(node_being_tested.state)
        if actions:
            stats["expanded"] += 1

        for action in reversed(actions):
            new_state = problem.result(node_being_tested.state, action)
            new_node = Node(new_state, node_being_tested, action)
            stats["total"] += 1
            frontier.append(new_node)
            if stats["max_frontier"] < len(frontier):
                stats["max_frontier"] = len(frontier)

    if cutoff:
        return "cutoff"
    else:
        return "failure"


#####################################################################################################################################

def ids(problem, L):
    #call dfs until set limit L
    for limit in range(L):
        start_node = Node(problem.init_state)
        result = dls(problem, L)

        if result is not "cutoff":
            return result
        
    return None


