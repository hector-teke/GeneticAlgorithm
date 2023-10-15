import random


# Generation of first generation of 50 solutions
def first_gen(length=50, population=50):
    solutions = dict() #Solutions are stored with their quality value

    for i in range(population):

        s = ""
        for j in range(length):
            s += str(random.randint(0, 1))

        solutions[s] = None

    evaluate()
    return solutions


# Evaluation with quality function

def evaluate(solutions, function):
    pass


print(first_gen())
