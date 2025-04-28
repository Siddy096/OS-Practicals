def sjf_non_preemptive(processes):
    n = len(processes)
    proc = sorted(processes, key=lambda x: (x['arrival'], x['burst']))

    wait_time = [0]*n
    turnaroundtime = [0]*n
    completiontime = [0]*n
    responsetime = [0]*n

    completiontime[0] = proc[0]['arrival'] + proc[0]['burst']
    turnaroundtime[0] = completiontime[0] - proc[0]['arrival']
    wait_time[0] = turnaroundtime[0] - proc[0]['burst']
    responsetime[0] = wait_time[0]

    for i in range(1, n):
        execution_time = max(proc[i]['arrival'], completiontime[i-1])
        completiontime[i] = execution_time + proc[i]['burst']
        turnaroundtime[i] = completiontime[i] - proc[i]['arrival']
        wait_time[i] = turnaroundtime[i] - proc[i]['burst']
        responsetime[i] = wait_time[i]

    print("\nAvg Waiting Time is: ", sum(wait_time) / n)
    print("\nAvg Turnaround Time is: ", sum(turnaroundtime) / n)
    print("Avg Response Time is: ", sum(responsetime) / n)

processes = [{"arrival": 0, "burst": 2},
             {"arrival": 1, "burst": 4},
             {"arrival": 2, "burst": 8},
             {"arrival": 3, "burst": 1},
             {"arrival": 4, "burst": 3},
             {"arrival": 5, "burst": 5}]

sjf_non_preemptive(processes)
