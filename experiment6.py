# def first_fit(block_size, process_size):
#     allocation = [-1] * len(process_size)
    
#     for i in range(len(process_size)):
#         for j in range(len(block_size)):
#             if block_size[j] >= process_size[i]:
#                 allocation[i] = j
#                 block_size[j] -= process_size[i]
#                 break
#     return allocation

# def best_fit(block_size, process_size):
#     allocation = [-1] * len(process_size)
    
#     for i in range(len(process_size)):
#         best_idx = -1
#         for j in range(len(block_size)):
#             if block_size[j] >= process_size[i]:
#                 if best_idx == -1 or block_size[j] < block_size[best_idx]:
#                     best_idx = j
#         if best_idx != -1:
#             allocation[i] = best_idx
#             block_size[best_idx] -= process_size[i]
#     return allocation

# def worst_fit(block_size, process_size):
#     allocation = [-1] * len(process_size)
    
#     for i in range(len(process_size)):
#         worst_idx = -1
#         for j in range(len(block_size)):
#             if block_size[j] >= process_size[i]:
#                 if worst_idx == -1 or block_size[j] > block_size[worst_idx]:
#                     worst_idx = j
#         if worst_idx != -1:
#             allocation[i] = worst_idx
#             block_size[worst_idx] -= process_size[i]
#     return allocation

# block_size = list(map(int, input("Enter block sizes (space separated): ").split()))
# process_size = list(map(int, input("Enter process sizes (space separated): ").split()))

# first_fit_alloc = first_fit(block_size.copy(), process_size)
# best_fit_alloc = best_fit(block_size.copy(), process_size)
# worst_fit_alloc = worst_fit(block_size.copy(), process_size)

# def print_allocation(method, allocation):
#     print(f"\n{method} Allocation:")
#     for i in range(len(process_size)):
#         if allocation[i] != -1:
#             print(f"Process {i} of size {process_size[i]} -> Block {allocation[i]}")
#         else:
#             print(f"Process {i} of size {process_size[i]} -> Not Allocated")

# print_allocation("First Fit", first_fit_alloc)
# print_allocation("Best Fit", best_fit_alloc)
# print_allocation("Worst Fit", worst_fit_alloc)

#First Fit:
blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

for i in range(len(processes)):
    for j in range(len(blocks)):
        if blocks[j] >= processes[i]:
            print(f"Process {processes[i]} -> Block {j + 1}")
            blocks[j] -= processes[i]
            break
    else:
        print(f"Process {processes[i]} -> Not Allocated")

# Best Fit
blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

for i in range(len(processes)):
    best = -1
    for j in range(len(blocks)):
        if blocks[j] >= processes[i]:
            if best == -1 or blocks[j] < blocks[best]:
                best = j
    if best != -1:
        print(f"Process {processes[i]} -> Block {best + 1}")
        blocks[best] -= processes[i]
    else:
        print(f"Process {processes[i]} -> Not Allocated")

# Worst Fit:
blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

for i in range(len(processes)):
    worst = -1
    for j in range(len(blocks)):
        if blocks[j] >= processes[i]:
            if worst == -1 or blocks[j] > blocks[worst]:
                worst = j
    if worst != -1:
        print(f"Process {processes[i]} -> Block {worst + 1}")
        blocks[worst] -= processes[i]
    else:
        print(f"Process {processes[i]} -> Not Allocated")

#Next Fit:
blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

pos = 0  # Start position

for i in range(len(processes)):
    allocated = False
    count = 0  # To prevent infinite loop
    while count < len(blocks):
        if blocks[pos] >= processes[i]:
            print(f"Process {processes[i]} -> Block {pos + 1}")
            blocks[pos] -= processes[i]
            allocated = True
            break
        pos = (pos + 1) % len(blocks)  # Move to next block
        count += 1
    if not allocated:
        print(f"Process {processes[i]} -> Not Allocated")
