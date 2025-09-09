from domains.problem import Problem
from node import Node
import heapq

def aStar(problem):
    startNode = Node(problem.init_state, None)
    problem.total_nodes += 1
    
    best_g = {tuple(startNode.state): 0}

    frontier = []
    id = 0

    h_cost = problem.heuristic0(startNode.state)
    f_cost = h_cost
    ## gonna add tuples to the frontier (f_cost, node)
    heapq.heappush(frontier, (f_cost, id, startNode))

    while frontier:
        print(f'TOTAL NUMBER OF NODES GENERATED: {problem.total_nodes}')
        print(f"frontier length is {len(frontier)}")
        _, _, node_being_tested = heapq.heappop(frontier)
        current_state = tuple(node_being_tested.state)
        if node_being_tested.depth > best_g[current_state]:
            continue

        print(f'goal testing {node_being_tested}...')
        if problem.GoalTest(node_being_tested.state):
            print("win")
            return (node_being_tested.state)
        
        problem.nodes_expanded += 1
        print(f"\n--- Expanding Node with state {current_state} and g_cost {node_being_tested.depth} ---")

        for action in problem.Actions(node_being_tested.state):
            new_state = problem.Transition(node_being_tested.state, action)
            new_state = tuple(new_state)

            #update g
            new_g = node_being_tested.depth + 1
            print(f"  Action: '{action}' -> New State: {new_state}")
            print(f"  Checking if {new_g} < {best_g.get(new_state, float('inf'))}")


            if new_g < best_g.get(new_state, float('inf')):
                print("  Condition MET. Adding node to frontier.")
                best_g[new_state] = new_g
                new_node = Node(new_state, node_being_tested, action)
                problem.total_nodes += 1

                new_h = problem.heuristic0(new_state)
                new_f = new_g + new_h

                id += 1

                heapq.heappush(frontier, (new_f, id, new_node))

                if problem.max_frontier < len(frontier):
                    problem.max_frontier = len(frontier)
    print("failed")
    return 