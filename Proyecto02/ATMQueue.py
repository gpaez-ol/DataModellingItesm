import random

def main():
    customers_n = int(input("How many customers?\n"))
    between_time_max = int(input("What's the max time between customers?\n"))
    transaction_time_max = int(input("What's the max transaction time?\n"))

    between_times = []
    transaction_times = []

    for _ in range(0,customers_n):
        between_times.append(random.randint(0, between_time_max))
        transaction_times.append(random.randint(1, transaction_time_max))
    
    starting_time = 540 # 9:00 AM
    arrival_times = []

    for i in range(0, customers_n):
        break
    


main()