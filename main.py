import random

from functions import ObjFunction


# Generation of first generation of 50 solutions with their quality value
def first_gen(function, length=50, population=50):
    solutions = dict()      # Solutions are stored with their quality value

    while len(solutions) < population:      # If a solution is repeated it is discarded
        s = ""
        for j in range(length):
            s += str(random.randint(0, 1))

        solutions[s] = None

    return evaluate(solutions, function)


# Evaluation with quality function
def evaluate(solutions, function):
    for s in solutions.keys():
        if solutions[s] is None:            # Just evaluates the new ones
            solutions[s] = function(s)
    return solutions









if __name__ == '__main__':

    f = ObjFunction()

    print(first_gen(f.f1))
    print(len(first_gen(f.f1)))
