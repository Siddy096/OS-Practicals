# # Priority Scheduling - Simple Python Code

# processes = [1, 2, 3]
# burst_time = [10, 1, 2]
# priority = [3, 1, 2]  # Lower number = higher priority

# # Combine everything and sort by priority
# combined = list(zip(processes, burst_time, priority))
# combined.sort(key=lambda x: x[2])  # sort by priority

# # Unpack after sorting
# processes, burst_time, priority = zip(*combined)

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
# print("Process\tBT\tPri\tWT\tTAT")
# for i in range(n):
#     print(f"P{processes[i]}\t{burst_time[i]}\t{priority[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")

process = [1,3,2]
burst_time = [10,1,2]
priority = [1,5,3]  #Lower Number = Higher Priority

combined = list(zip(process, burst_time, priority))
combined.sort(key=lambda x: x[2])
process, burst_time, priority = zip(*combined)

n = len(process)
wait_time = [0]*n
turnaround_time = [0]*n

for i in range(1,n):
    wait_time[i] = wait_time[i-1] + burst_time[i-1]

for i in range(n):
    turnaround_time[i] = wait_time[i] + burst_time[i]

print("\tProcess\tBT\tWT\tP\tTAT")
for i in range(n):
    print(f"\t{process[i]}\t{burst_time[i]}\t{wait_time[i]}\t{priority[i]}\t{turnaround_time[i]}")