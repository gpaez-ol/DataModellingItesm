import random
import numpy as np

n = int(input("N?\n"))

markov = []
warriors = []
attack_chances = []

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
    print("{a:<{spacing}}".format(a="",spacing=spacing), end='')
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

def remove_state(mat, n):
    rows = len(mat)
    columns = len(mat[0])
    for j in range(0, columns):
        mat[n][j] = 0.0
    for i in range(0, rows):
        mat[i][n] = 0.0
        row_sum = sum(mat[i])
        if row_sum > 0.0:
            for j in range(0, columns):
                mat[i][j] /= row_sum
    return mat

def generate_attack_chances(n):
    output = []
    for _ in range(0,n):
        output.append(1.0 / n)
    return output

def remove_attack_chance(arr, i):
    arr[i] = 0.0
    total = sum(arr)
    if total > 0:
        for i in range(0, len(arr)):
            arr[i] /= total
    return arr

def choose_from_row(arr):
    output = np.random.choice(a=range(0, len(arr)), size=1, p=arr)
    return output[0]

markov = generate_random_markov(n)
warriors = generate_warriors(n, 10, 100)
attack_chances = generate_attack_chances(n)

print_matrix(markov)
print(warriors)
print(attack_chances)

remove_state(markov, 2)
print_matrix(markov)

print(remove_attack_chance(attack_chances, 2))

remove_state(markov, 1)
print_matrix(markov)

print(remove_attack_chance(attack_chances, 1))

print(choose_from_row(attack_chances))