import random

#test_between_times = [0,1,10,1,10,8,2,10,2,3]
#test_transaction_times = [4,1,5,4,2,3,2,1,3,2]

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

    #between_times = test_between_times
    #transaction_times = test_transaction_times
    #customers_n = 10

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

    # printing results
    total_atm_time = service_end_times[customers_n - 1] - starting_time
    total_transaction_time = sum(transaction_times)
    total_idle_time = sum(idling_times)
    total_wait = 0
    waiting_customers = 0
    for i in range(0, customers_n):
        if wait_times[i] > 0:
            waiting_customers += 1
            total_wait += wait_times[i]
    result_str = "Average wait time: {}".format(total_wait / customers_n)
    result_str += "\nProbability to wait in queue: {:.2f}%".format(waiting_customers / customers_n * 100)
    result_str += "\nIdle time percentage: {:.2f}%".format(total_idle_time / total_atm_time * 100)
    result_str += "\nAverage service time: {}".format(total_transaction_time / customers_n)

    print(result_str)

    f1 = open("output_table.txt", "w")
    f1.write(table_str)
    f1.close()

    f2 = open("output_results.txt", "w")
    f2.write(result_str)
    f2.close()

main()