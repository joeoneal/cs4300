from search import bfs
from domains.wgc import WGC
import helpers

def main():
    problem = WGC()
    solution = bfs(problem) ## solution is a tuple --> node is index 0, index 1-3 contain other info
    print()
    print("Domain: WGC | Algorithm: BFS")
    print(f'Solution Cost: {solution[0].depth} | Depth: {solution[0].depth}')
    print(f'Nodes generated: {solution[1]} | Nodes expanded: {solution[2]} | Max frontier: {solution[3]}')

    path = helpers.find_path(solution[0])

    print()

    print("State key: [Wolf, Goat, Cabbage, Farmer]")
    print()
    print("Path:")

    for i in range(len(path) - 1):
        n1 = path[i]
        n2 = path[i+1]
        counter = i+1

        action = helpers.format(n2.action).ljust(12)

        print(f'{counter}) {action} {n1.state} --> {n2.state}')

    print()

    ################
    #dfs test
    problem2 = WGC()
    solution2 = bfs(problem2) ## solution is a tuple --> node is index 0, index 1-3 contain other info
    print()
    print("Domain: WGC | Algorithm: BFS")
    print(f'Solution Cost: {solution2[0].depth} | Depth: {solution2[0].depth}')
    print(f'Nodes generated: {solution2[1]} | Nodes expanded: {solution2[2]} | Max frontier: {solution2[3]}')



if __name__ == "__main__":
    main()