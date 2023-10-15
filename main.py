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

# Roulette selection: selects 2 mutually different parents from the set of solutions
def roulette(solutions):
    pa1 = None
    pa2 = None
    total = sum(solutions.values())

    rnum = random.randint(0, total)

    i = 0
    for k in solutions.keys():
        i += solutions[k]
        if i >= rnum:
            pa1 = k
            break

    while True:     # Avoid the problem of choosing the same parents

        rnum = random.randint(0, total)

        i = 0
        for k in solutions.keys():
            i += solutions[k]
            if i >= rnum:
                pa2 = k
                break

        if pa1 != pa2:  # Check that the parents are different
            break

    return pa1, pa2


# One-point crossover of two parents -> two childrens
def crossover(pa1, pa2):
    point = random.randint(0, len(pa1))

    new1 = pa1[0:point] + pa2[point:len(pa2)]
    new2 = pa2[0:point] + pa1[point:len(pa1)]

    return new1, new2










if __name__ == '__main__':

    f = ObjFunction()

    s = first_gen(f.f1)

    print(s)

    s = next_gen(s)

    print(s)

    pa1, pa2 = roulette(s)

    print("PA1: ", pa1)
    print("PA2: ", pa2)

    new1, new2 = crossover(pa1, pa2)

    print("HI1: ", new1)
    print("HI2: ", new2)

