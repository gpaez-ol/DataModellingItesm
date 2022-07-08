def lehmer(x0, a, c, m, n):
    last_val = x0
    output = []
    for _ in range(0, n):
        new_val = (a * last_val + c) % m
        output.append(new_val / m)
        last_val = new_val
    return output
print("The numbers are: ",lehmer(6,32,3,80,10))