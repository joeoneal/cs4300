from search import aStar
from domains.problem import Problem

def main():
    totalne = 0
    totalng = 0
    totalfs = 0
    totalsd = 0
    for i in range(30):
        problem = Problem()
        solution = aStar(problem)
        # print(f'\nnodes expanded: {solution[0]} ')
        # print(f'nodes generated: {solution[1]}')
        # print(f'max frontier size: {solution[2]}')
        # print(f'solution depth/cost: {solution[3]}')
        totalne += solution[0]
        totalng += solution[1]
        totalfs += solution[2]
        totalsd += solution[3]
    avg_ne = totalne / 3
    avg_ng = totalng / 3
    avg_fs = totalfs / 3
    avg_sd = totalsd / 3

    print(f'\nAverage nodes expanded: {solution[0]} ')
    print(f'Average number of nodes generated: {solution[1]}')
    print(f'Average max frontier size: {solution[2]}')
    print(f'Average solution depth/cost: {solution[3]}')
    
        

if __name__ == "__main__":
    main()