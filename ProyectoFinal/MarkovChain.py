import random

n = int(input("N?\n"))

markov = []

def generate_random_markov(n):
    output : list[list[float]] = []
    for i in range(0,n):
        output.append([])
        for j in range(0,n):
            if i == j:
                output[i].append(0.0)
            else:
                output[i].append(random.random())
        row_total = sum(output[i])
        for j in range(0,n):
            output[i][j] /= row_total
    return output

def print_matrix(mat):
    for i in range(0, len(mat)):
        for j in range(0, len(mat[i])):
            print("{:4f} ".format(mat[i][j]), end='')
        print("")

markov = generate_random_markov(n)
print_matrix(markov)