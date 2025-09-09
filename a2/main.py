from search import aStar
from domains.problem import Problem

def main():


    for i in range(3):

        print(f'RUNNING WITH HEURISTIC{i}')
        totalne = 0
        totalng = 0
        totalfs = 0
        totalsd = 0
        for _ in range(30):
            problem = Problem()
            heuristics_to_test = [
                problem.heuristic0, 
                problem.heuristic1, 
                problem.heuristic2
            ]

            h_func = heuristics_to_test[i]
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

        print(f'\nAverage nodes expanded: {round(avg_ne, 2)} ')
        print(f'Average number of nodes generated: {round(avg_ng, 2)}')
        print(f'Average max frontier size: {round(avg_fs, 2)}')
        print(f'Average solution depth/cost: {round(avg_sd,2)}')
        print()
    
        

if __name__ == "__main__":
    main()