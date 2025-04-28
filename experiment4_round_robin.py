def round_robin_scheduling(processes, time_quantum):
    total_time = 0
    total_time_counted = 0
    wait_time = 0
    turnaround_time = 0
    response_time = 0

    proc = []
    for process in processes:
        arrival, burst = process['arrival'], process['burst']
        proc.append([arrival, burst, burst, 0, 0, -1])
        total_time += burst

    while total_time != 0:
        for i in range(len(proc)):
            if proc[i][2] <= time_quantum and proc[i][2] >= 0:
                total_time_counted += proc[i][2]
                total_time -= proc[i][2]
                proc[i][2] = 0
            elif proc[i][2] > 0:
                proc[i][2] -= time_quantum
                total_time -= time_quantum
                total_time_counted += time_quantum
            if proc[i][2] == 0 and proc[i][3] != 1:
                wait_time += total_time_counted - proc[i][1]
                turnaround_time += total_time_counted - proc[i][0]
                proc[i][3] = 1
            if proc[i][2] != 0 and proc[i][5] == -1:
                proc[i][5] = total_time_counted - proc[i][0]
                response_time += proc[i][5]

    print("\nAvg Waiting Time is ", (wait_time * 1) / len(processes))
    print("Avg Turnaround Time is ", (turnaround_time * 1) / len(processes))
    print("Avg Response Time is ", (response_time * 1) / len(processes))

processes = [
    {"arrival": 0, "burst": 2},
    {"arrival": 1, "burst": 4},
    {"arrival": 1, "burst": 8},
    {"arrival": 2, "burst": 1},
    {"arrival": 4, "burst": 3},
    {"arrival": 5, "burst": 5}
]

round_robin_scheduling(processes, 2)
