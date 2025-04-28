def is_safe(processes, avail, max_need, allot):
    n = len(processes)
    m = len(avail)
    
    need = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            need[i][j] = max_need[i][j] - allot[i][j]
    
    finish = [False] * n
    safe_seq = []
    work = avail.copy()

    while len(safe_seq) < n:
        found = False
        for i in range(n):
            if not finish[i]:
                if all(need[i][j] <= work[j] for j in range(m)):
                    for j in range(m):
                        work[j] += allot[i][j]
                    safe_seq.append(processes[i])
                    finish[i] = True
                    found = True
        if not found:
            return False, []
    
    return True, safe_seq

n = int(input("Enter number of processes: "))
m = int(input("Enter number of resource types: "))

processes = list(range(n))

available = list(map(int, input(f"Enter available resources ({m} values): ").split()))

print("Enter maximum resources needed for each process:")
maximum_need = []
for i in range(n):
    max_row = list(map(int, input(f"Process {i}: ").split()))
    maximum_need.append(max_row)

print("Enter allocated resources for each process:")
allocation = []
for i in range(n):
    alloc_row = list(map(int, input(f"Process {i}: ").split()))
    allocation.append(alloc_row)

safe, sequence = is_safe(processes, available, maximum_need, allocation)

if safe:
    print("\nSystem is in a SAFE state.")
    print("Safe sequence:", ' -> '.join(f"P{p}" for p in sequence))
else:
    print("\nSystem is NOT in a safe state.")