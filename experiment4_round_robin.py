# Round Robin Scheduling - Simple Python Code

# processes = [1, 2, 3]
# burst_time = [5, 15, 4]
# quantum = 4

# n = len(processes)
# remaining_time = burst_time[:]
# waiting_time = [0] * n
# t = 0  # current time

# while True:
#     done = True
#     for i in range(n):
#         if remaining_time[i] > 0:
#             done = False
#             if remaining_time[i] > quantum:
#                 t += quantum
#                 remaining_time[i] -= quantum
#             else:
#                 t += remaining_time[i]
#                 waiting_time[i] = t - burst_time[i]
#                 remaining_time[i] = 0
#     if done:
#         break

# turnaround_time = [waiting_time[i] + burst_time[i] for i in range(n)]

# # Print result
# print("Process\tBT\tWT\tTAT")
# for i in range(n):
#     print(f"P{processes[i]}\t{burst_time[i]}\t{waiting_time[i]}\t{turnaround_time[i]}")

process = [1,2,3]
burst_time = [5,15,4]
quantum = 4
remaining_time = burst_time[:]

n = len(process)
t = 0
wait_time = [0]*n
turnaround_time = [0]*n

while True:
    done = True
    for i in range(n):
        if remaining_time[i] > 0:
            done = False
            for i in range(n):
                if remaining_time[i] > quantum:
                    t += quantum
                    remaining_time[i] -= quantum
                else:
                    t += remaining_time[i]
                    wait_time[i] = t - burst_time[i]
                    remaining_time[i] = 0
    if done:
        break
for i in range(n):
    turnaround_time[i] = wait_time[i] + burst_time[i]

print("\tProcess\tBT\tWT\tTAT\tQ")
for i in range(n):
    print(f"\t{process[i]}\t{burst_time[i]}\t{wait_time[i]}\t{turnaround_time[i]}\t{quantum}")