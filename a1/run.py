from search import bfs

def main():
    solution = bfs() ## solution is a tuple --> node is index 0, index 1-3 contain other info
    print()
    print("Domain: WGC | Algorithm: BFS")
    print(f'Solution Cost: {solution[0].depth} | Depth: {solution[0].depth}')
    print(f'Nodes generated: {solution[1]} | Nodes expanded: {solution[2]} | Max frontier: {solution[3]}')




if __name__ == "__main__":
    main()