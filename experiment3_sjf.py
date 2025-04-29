# # SJF Scheduling - Simple Python Code (Non-Preemptive, No Arrival Time)

# processes = [1, 2, 3]
# burst_time = [6, 8, 7]

# # Combine processes and burst times
# combined = list(zip(processes, burst_time))

# # Sort by burst time (Shortest Job First)
# combined.sort(key=lambda x: x[1])

# # Extract sorted process IDs and burst times
# processes, burst_time = zip(*combined)

# n = len(processes)
# waiting_time = [0] * n
# turnaround_time = [0] * n

# # Calculate waiting time
# for i in range(1, n):
#     waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1]

# # Calculate turnaround time
# for i in range(n):
#     turnaround_time[i] = waiting_time[i] + burst_time[i]

# # Print result
# print("Process\tBT\tWT\tTAT")
# for i in range(n):
#     print(f"P{processes[i]}\t{burst_time[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")

process = [1,3,2]
burst_time = [6,8,7]

combined = list(zip(process, burst_time))
combined.sort(key=lambda x: x[1])
process, burst_time = zip(*combined)

n = len(process)
wait_time = [0]*n
turnaround_time = [0]*n

for i in range(1,n):
    wait_time[i] = wait_time[i-1] + burst_time[i-1]

for i in range(n):
    turnaround_time[i] = wait_time[i] + burst_time[i]

print("\tProcess\tBT\tWT\tTAT")

for i in range(n):
    print(f"\t{process[i]}\t{burst_time[i]}\t{wait_time[i]}\t{turnaround_time[i]}")