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

