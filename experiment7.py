def fifo(pages, capacity):
    frame = []
    page_faults = 0
    
    for page in pages:
        if page not in frame:
            if len(frame) < capacity:
                frame.append(page)
            else:
                frame.pop(0)
                frame.append(page)
            page_faults += 1
    return page_faults

def lru(pages, capacity):
    frame = []
    page_faults = 0
    
    for page in pages:
        if page not in frame:
            if len(frame) < capacity:
                frame.append(page)
            else:
                frame.pop(0)
                frame.append(page)
            page_faults += 1
        else:
            frame.remove(page)
            frame.append(page)
    return page_faults

def optimal(pages, capacity):
    frame = []
    page_faults = 0

    for i in range(len(pages)):
        if pages[i] not in frame:
            if len(frame) < capacity:
                frame.append(pages[i])
            else:
                farthest = -1
                index = -1
                for j in range(len(frame)):
                    try:
                        next_use = pages[i+1:].index(frame[j])
                    except ValueError:
                        next_use = float('inf')
                    if next_use > farthest:
                        farthest = next_use
                        index = j
                frame[index] = pages[i]
            page_faults += 1
    return page_faults

pages = list(map(int, input("Enter page reference string (space separated): ").split()))
capacity = int(input("Enter number of frames: "))

print("\nPage Faults:")
print("FIFO:", fifo(pages, capacity))
print("LRU:", lru(pages, capacity))
print("Optimal:", optimal(pages, capacity))