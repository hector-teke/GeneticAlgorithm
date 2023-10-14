import random

# Generation of first generation of 50 solutions
def first_gen(length=50, population=50):
    solutions = []

    for i in range(population):

        s = ""
        for j in range(length):
            s += str(random.randint(0, 1))

        solutions.append(s)

    return solutions

# Evaluation with quality function

    # mirar si se puede pasar la funcion objetiva por parametros para asi solo hacer una evaluacion
