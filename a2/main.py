from search import aStar
from domains.problem import Problem

def main():
    problem = Problem()
    solution = aStar(problem)
    print(f'\nnodes expanded: {solution[0]} ')
    print(f'nodes generated: {solution[1]}')
    print(f'max frontier size: {solution[2]}')
    print(f'solution depth/cost: {solution[3]}')

if __name__ == "__main__":
    main()