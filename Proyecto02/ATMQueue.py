import random

def get_time_string(n):
    hours = n // 60
    mins = n % 60

    suffix = ""
    if hours <= 12:
        suffix = "AM"
    else:
        suffix = "PM"
    
    if (hours == 0):
        hours = 12
    
    if (mins < 10):
        mins = "0{}".format(mins)

    return "{}:{} {}".format(hours, mins, suffix)

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
    idling_times = []

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
        idling_times.append(service_start_times[i] - last_service_end_time)

        last_service_end_time = service_end_times[i]
        last_arrival_time = arrival_times[i]

    # printing table
    spacing = 15
    row_format = "{customer:<{spacing}}{between:<{spacing}}{arrival:<{spacing}}{transaction:<{spacing}}{start:<{spacing}}{end:<{spacing}}{wait:<{spacing}}{idle}"
    table_str = row_format.format(customer="Customer", between="Time between", arrival="Arrival", transaction="Transaction", start="Start", end="End", wait="Waiting", idle="ATM idling", spacing=spacing)
    for i in range(0, customers_n):
        row_str = row_format.format(customer=i+1, between=between_times[i], arrival=get_time_string(arrival_times[i]), transaction=transaction_times[i], start=get_time_string(service_start_times[i]), end=get_time_string(service_end_times[i]), wait=wait_times[i], idle=idling_times[i], spacing=spacing)
        table_str += "\n{}".format(row_str)
    
    print(table_str)

main()