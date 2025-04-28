def first_fit(block_size, process_size):
    allocation = [-1] * len(process_size)
    
    for i in range(len(process_size)):
        for j in range(len(block_size)):
            if block_size[j] >= process_size[i]:
                allocation[i] = j
                block_size[j] -= process_size[i]
                break
    return allocation

def best_fit(block_size, process_size):
    allocation = [-1] * len(process_size)
    
    for i in range(len(process_size)):
        best_idx = -1
        for j in range(len(block_size)):
            if block_size[j] >= process_size[i]:
                if best_idx == -1 or block_size[j] < block_size[best_idx]:
                    best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
            block_size[best_idx] -= process_size[i]
    return allocation

def worst_fit(block_size, process_size):
    allocation = [-1] * len(process_size)
    
    for i in range(len(process_size)):
        worst_idx = -1
        for j in range(len(block_size)):
            if block_size[j] >= process_size[i]:
                if worst_idx == -1 or block_size[j] > block_size[worst_idx]:
                    worst_idx = j
        if worst_idx != -1:
            allocation[i] = worst_idx
            block_size[worst_idx] -= process_size[i]
    return allocation

block_size = list(map(int, input("Enter block sizes (space separated): ").split()))
process_size = list(map(int, input("Enter process sizes (space separated): ").split()))

first_fit_alloc = first_fit(block_size.copy(), process_size)
best_fit_alloc = best_fit(block_size.copy(), process_size)
worst_fit_alloc = worst_fit(block_size.copy(), process_size)

def print_allocation(method, allocation):
    print(f"\n{method} Allocation:")
    for i in range(len(process_size)):
        if allocation[i] != -1:
            print(f"Process {i} of size {process_size[i]} -> Block {allocation[i]}")
        else:
            print(f"Process {i} of size {process_size[i]} -> Not Allocated")

print_allocation("First Fit", first_fit_alloc)
print_allocation("Best Fit", best_fit_alloc)
print_allocation("Worst Fit", worst_fit_alloc)