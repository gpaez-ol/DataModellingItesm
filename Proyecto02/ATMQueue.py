import random

def get_time_string(n):
    hours = n / 60
    mins = n % 60
    return "{}:{}".format(hours, mins)

def main():
    customers_n = int(input("How many customers?\n"))
    between_time_max = int(input("What's the max time between customers?\n"))
    transaction_time_max = int(input("What's the max transaction time?\n"))

    between_times = []
    transaction_times = []
    
    starting_time = 540 # 9:00 AM
    last_service_end_time = starting_time
    last_arrival_time = starting_time
    arrival_times = []
    service_start_times  = []
    service_end_times = []
    wait_times = []
    inactivity_times = []

    def generate_between_time():
        return random.randint(0, between_time_max)
    
    def generate_transaction_time():
        return random.randint(1, transaction_time_max)

    for i in range(0,customers_n):        
        between_times.append(generate_between_time())
        transaction_times.append( generate_transaction_time())
        
        arrival_times.append(last_arrival_time + between_times[i])
        
        if arrival_times[i] > last_service_end_time:
            service_start_times.append(arrival_times[i])
        else:
            service_start_times.append(last_service_end_time)
        
        service_end_times.append(service_start_times[i] + transaction_times[i])

        wait_times.append(service_start_times[i] - arrival_times[i])
        inactivity_times.append(service_start_times[i] - last_service_end_time)

        last_service_end_time = service_end_times[i]
        last_arrival_time = arrival_times[i]

    print(between_times)
    print(arrival_times)
    print(transaction_times)
    print(service_start_times)
    print(service_end_times)
    print(wait_times)
    print(inactivity_times)

main()