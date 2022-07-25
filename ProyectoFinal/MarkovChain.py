import random

n = int(input("N?\n"))

markov = []
warriors = []

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
    decimals = 4
    spacing = decimals + 3
    rows = len(mat)
    print("{:<{spacing}}".format("",spacing=spacing), end='')
    for i in range(0, rows):
        print("{i:<{spacing}}".format(i=i, spacing=spacing), end='')
    print("")
    for i in range(0, rows):
        print("{i:<{spacing}}".format(i=i, spacing=spacing), end='')
        for j in range(0, len(mat[i])):
            print("{value:.{decimals}f} ".format(value=mat[i][j], decimals=decimals), end='')
        print("")

def generate_warriors(n, min, max):
    output = []
    for _ in range(0, n):
        output.append(random.randint(min, max))
    return output

markov = generate_random_markov(n)
warriors = generate_warriors(n, 10, 100)

print_matrix(markov)
print(warriors)