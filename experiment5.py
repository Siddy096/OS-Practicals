# Banker's Algorithm - Deadlock Avoidance (Short Version)

n = 3  # Number of processes
m = 3  # Number of resources

# Example data
alloc = [[0, 1, 0], 
         [2, 0, 0], 
         [3, 0, 2]]

max_need = [[7, 5, 3], 
            [3, 2, 2], 
            [9, 0, 2]]

avail = [3, 3, 2]

# Calculate need matrix
need = [[max_need[i][j] - alloc[i][j]for j in range(m)]for i in range(n)]

finish = [False] * n
safe_seq = []

while len(safe_seq) < n:
    found = False
    for i in range(n):
        if not finish[i] and all(need[i][j] <= avail[j] for j in range(m)):
            for j in range(m):
                avail[j] += alloc[i][j]
            finish[i] = True
            safe_seq.append(i)
            found = True
            break
    if not found:
        break

if len(safe_seq) == n:
    print("System is in a safe state.")
    print("Safe sequence:", ' -> '.join(f'P{i}' for i in safe_seq))
else:
    print("System is in an unsafe state (deadlock possible).")
