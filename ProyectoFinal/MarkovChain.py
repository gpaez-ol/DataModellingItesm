import random
import numpy as np

n = int(input("N?\n"))

markov = []
warriors = []
groups = []

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

def matrix_string(mat, groups):
    output = ""
    decimals = 4
    spacing = decimals + 3
    rows = len(mat)
    output += "{a:<{spacing}}".format(a="",spacing=spacing)
    for i in range(0, rows):
        output += "{i:<{spacing}}".format(i=groups[i], spacing=spacing)
    output += '\n'
    for i in range(0, rows):
        output += "{i:<{spacing}}".format(i=groups[i], spacing=spacing)
        for j in range(0, len(mat[i])):
            output += "{value:.{decimals}f} ".format(value=mat[i][j], decimals=decimals)
        output += '\n'
    return output

def generate_warriors(n, min, max):
    output = []
    for _ in range(0, n):
        output.append(random.randint(min, max))
    return output

def remove_group(mat : list[list[float]], groups : list[int], warriors : list[int], n : int):
    
    mat.pop(n)
    groups.pop(n)
    warriors.pop(n)

    rows = len(mat)

    for i in range(0, rows):
        mat[i].pop(n)

    columns = len(mat[0])

    for i in range(0, rows):
        row_sum = sum(mat[i])
        if row_sum > 0.0:
            for j in range(0, columns):
                mat[i][j] /= row_sum
    return mat

def choose_from_row(arr):
    output = np.random.choice(a=range(0, len(arr)), size=1, p=arr)
    return output[0]

def generate_groups(n):
    output = list(range(1,n+1))
    return output


markov = generate_random_markov(n)
warriors = generate_warriors(n, 10, 100)
groups = generate_groups(n)

print(matrix_string(markov, groups))
print(warriors)
print(groups)

remove_group(markov, groups, warriors, 2)
print(matrix_string(markov, groups))
print(groups)

remove_group(markov, groups, warriors, 1)
print(matrix_string(markov, groups))
print(groups)