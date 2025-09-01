def find_path(node):
    path = []
    while node:
        path.append(node)
        node = node.parent
    return path[::-1]

def format(action):
    if action == (3, ):
        return "Move Alone"
    
    ent = {0: "Wolf", 1: "Goat", 2: "Cabbage"}
    moved = ent.get(action[1])
    return f'Move {moved}'

def print_and_format(solution, domain, algo):
    print(f"Domain: {domain.upper()} | Algorithm: {algo.upper()}")
    print(f'Solution Cost: {solution[0].depth} | Depth: {solution[0].depth}')
    print(f'Nodes generated: {solution[1]} | Nodes expanded: {solution[2]} | Max frontier: {solution[3]}')

    path = find_path(solution[0])

    print()

    print("State key: [Wolf, Goat, Cabbage, Farmer]")
    print()
    print("Path:")

    for i in range(len(path) - 1):
        n1 = path[i]
        n2 = path[i+1]
        counter = i+1

        action = format(n2.action).ljust(12)

        print(f'{counter}) {action} {n1.state} --> {n2.state}')

    print()