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

# Move best 20% of the population into the next generation
def next_gen (solutions, perc=20):
    values = sorted(solutions.values(), reverse=True)  # List of values from the highest
    size = int(len(values) * perc / 100)  # Size of survivors set

    nextgen = dict()

    for val in values[0:size]:

        key = None
        for k, v in solutions.items():    # Take the first key that has this value
            if v == val:
                key = k
                break

        nextgen[key] = val        # Add key-value to the new set of solutions
        solutions.pop(key)      # Removes key-value from original

    return nextgen


if __name__ == '__main__':

    f = ObjFunction()

    s = first_gen(f.f1)

    print(s)

    print(next_gen(s))

    # obtengo los valores
    # ordeno los valores
    # saco desde el valor mas alto hasta que no queden
