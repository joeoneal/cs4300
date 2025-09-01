from search import bfs, ids
from domains.wgc import WGC
import helpers
import argparse

## new main          --> moved all print logic to a helper function in helpers.py
##                   --> also added arg parse instead of sequentially doing both searches :)
##                   --> old main is commented out, too attached to delete it lol
def main():
    parser = argparse.ArgumentParser("run search alg")
    parser.add_argument("--domain", required=True, choices=["wgc"])
    parser.add_argument("--algo", required=True, choices=["bfs", "ids"])
    args = parser.parse_args()

    if args.domain == "wgc":
        problem = WGC()
    else:
        print("Unknown Domain")
        return
    
    solution = None

    if args.algo == "bfs":
        solution = bfs(problem)
    elif args.algo == "ids":
        solution = ids(problem, 20)

    helpers.print_and_format(solution, args.domain, args.algo)




# def main():
#     problem = WGC()
#     solution = bfs(problem) ## solution is a tuple --> node is index 0, index 1-3 contain other info
#     print()
#     print("Domain: WGC | Algorithm: BFS")
#     print(f'Solution Cost: {solution[0].depth} | Depth: {solution[0].depth}')
#     print(f'Nodes generated: {solution[1]} | Nodes expanded: {solution[2]} | Max frontier: {solution[3]}')

#     path = helpers.find_path(solution[0])

#     print()

#     print("State key: [Wolf, Goat, Cabbage, Farmer]")
#     print()
#     print("Path:")

#     for i in range(len(path) - 1):
#         n1 = path[i]
#         n2 = path[i+1]
#         counter = i+1

#         action = helpers.format(n2.action).ljust(12)

#         print(f'{counter}) {action} {n1.state} --> {n2.state}')

#     print()

#     ################
#     #dls test
#     problem2 = WGC()
#     solution2 = ids(problem2, 10) ## solution is a tuple --> node is index 0, index 1-3 contain other info
#     print()
#     print("Domain: WGC | Algorithm: IDS")
#     print(f'Solution Cost: {solution2[0].depth} | Depth: {solution2[0].depth}')
#     print(f'Nodes generated: {solution2[1]} | Nodes expanded: {solution2[2]} | Max frontier: {solution2[3]}')

#     path2 = helpers.find_path(solution[0])

#     print()

#     print("State key: [Wolf, Goat, Cabbage, Farmer]")
#     print()
#     print("Path:")

#     for i in range(len(path2) - 1):
#         n3 = path2[i]
#         n4 = path2[i+1]
#         counter = i+1

#         action2 = helpers.format(n4.action).ljust(12)

#         print(f'{counter}) {action2} {n3.state} --> {n4.state}')
    

if __name__ == "__main__":
    main()