import random

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

# returns index
def choose_from_row(arr):
    output = random.choices(population=range(0, len(arr)), weights=arr, k=1)
    return output[0]

def generate_groups(n):
    output = list(range(1,n+1))
    return output

# returns index
def choose_attacker(groups):
    output = random.choices(population=range(0, len(groups)), k=1)
    return output[0]

def group_warriors_string(groups, warriors):
    output = ""
    for i in range(0, len(groups)):
        output += "Group {group}: {population}\n".format(group=groups[i], population=warriors[i])
    return output

# print(matrix_string(markov, groups))
# print(warriors)
# print(groups)

# remove_group(markov, groups, warriors, 2)
# print(matrix_string(markov, groups))
# print(groups)

# remove_group(markov, groups, warriors, 1)
# print(matrix_string(markov, groups))
# print(groups)

def main():
    n = int(input("N?\n"))

    markov = generate_random_markov(n)
    warriors = generate_warriors(n, 10, 100)
    groups = generate_groups(n)

    output_file = open("output.txt", "a")
    def print_middleware(s, end='\n'):
        output_file.write("{s}{end}".format(s=s, end=end))
        print(s, end=end)

    print_middleware(matrix_string(markov, groups))

    while len(groups) > 1:
        attacker_index = choose_attacker(groups)
        attacked_index = choose_from_row(markov[attacker_index])
        print_middleware("Group {} attacked Group {}".format(groups[attacker_index], groups[attacked_index]))
        print_middleware("\nRemaining warriors")
        print_middleware(group_warriors_string(groups, warriors))
        remove_group(markov, groups, warriors, attacked_index)
        print_middleware(matrix_string(markov, groups))

    output_file.close()

main()