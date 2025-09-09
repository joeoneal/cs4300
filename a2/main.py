from search import aStar
from domains.problem import Problem

def main():
    problem = Problem()
    solution = aStar(problem)

    print()

if __name__ == "__main__":
    main()