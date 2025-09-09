from search import aStar
from domains.problem import Problem

def main():
    heuristics_to_test = [
        Problem.heuristic0, 
        Problem.heuristic1, 
        Problem.heuristic2
    ]

    for i in range(3):
        h_func = heuristics_to_test[i]
        print(f'RUNNING WITH HEURISTIC{i}')
        totalne = 0
        totalng = 0
        totalfs = 0
        totalsd = 0
        for i in range(30):
            problem = Problem()
            solution = aStar(problem, h_func)
            # print(f'\nnodes expanded: {solution[0]} ')
            # print(f'nodes generated: {solution[1]}')
            # print(f'max frontier size: {solution[2]}')
            # print(f'solution depth/cost: {solution[3]}')
            totalne += solution[0]
            totalng += solution[1]
            totalfs += solution[2]
            totalsd += solution[3]
        avg_ne = totalne / 30
        avg_ng = totalng / 30
        avg_fs = totalfs / 30
        avg_sd = totalsd / 30

        print(f'\nAverage nodes expanded: {avg_ne} ')
        print(f'Average number of nodes generated: {avg_ng}')
        print(f'Average max frontier size: {avg_fs}')
        print(f'Average solution depth/cost: {avg_sd}')
        print()
    
        

if __name__ == "__main__":
    main()