# # FCFS Scheduling - Simple Python Code

# # List of processes with their burst times
# processes = [1, 2, 3]
# burst_time = [5, 9, 6]

# n = len(processes)
# waiting_time = [0] * n
# turnaround_time = [0] * n

# # Calculate waiting time
# for i in range(1, n):
#     waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1]

# # Calculate turnaround time
# for i in range(n):
#     turnaround_time[i] = waiting_time[i] + burst_time[i]

# # Print results
# print("Process\tBT\tWT\tTAT")
# for i in range(n):
#     print(f"P{processes[i]}\t{burst_time[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")


processs = [1,2,3]
burst_time = [5,9,6]

n = len(processs)
waiting_time = [0]*n
turnaround_time = [0]*n

for i in range(1,n):
    waiting_time[i] = waiting_time[i-1] + burst_time[i-1]

for i in range(n):
    turnaround_time[i] = waiting_time[i] + burst_time[i]

print("Process\tBT\tWT\tTAT")
for i in range(n):
    print(f"P{processs[i]}\t{burst_time[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")