def fcfs(requests, head):
    seek_sequence = []
    total_seek = 0
    current = head
    
    for track in requests:
        seek_sequence.append(track)
        total_seek += abs(track - current)
        current = track
        
    return total_seek, seek_sequence

def scan(requests, head, disk_size, direction):
    seek_sequence = []
    total_seek = 0
    left = [track for track in requests if track < head]
    right = [track for track in requests if track >= head]
    
    left.sort()
    right.sort()
    
    run = True
    current = head
    
    if direction == "left":
        for track in reversed(left):
            seek_sequence.append(track)
            total_seek += abs(current - track)
            current = track
        if left:
            total_seek += abs(current - 0)
            current = 0
        for track in right:
            seek_sequence.append(track)
            total_seek += abs(current - track)
            current = track
    else:  # direction == "right"
        for track in right:
            seek_sequence.append(track)
            total_seek += abs(current - track)
            current = track
        if right:
            total_seek += abs((disk_size - 1) - current)
            current = disk_size - 1
        for track in reversed(left):
            seek_sequence.append(track)
            total_seek += abs(current - track)
            current = track
    
    return total_seek, seek_sequence

def c_scan(requests, head, disk_size):
    seek_sequence = []
    total_seek = 0
    left = [track for track in requests if track < head]
    right = [track for track in requests if track >= head]
    
    left.sort()
    right.sort()
    
    current = head
    
    for track in right:
        seek_sequence.append(track)
        total_seek += abs(current - track)
        current = track

    if current != disk_size - 1:
        total_seek += abs((disk_size - 1) - current)
        current = disk_size - 1

    total_seek += disk_size - 1
    current = 0

    for track in left:
        seek_sequence.append(track)
        total_seek += abs(current - track)
        current = track
    
    return total_seek, seek_sequence

requests = list(map(int, input("Enter disk track requests (space separated): ").split()))
head = int(input("Enter initial head position: "))
disk_size = int(input("Enter total disk size (number of tracks): "))

fcfs_seek, fcfs_seq = fcfs(requests, head)
print("\n--- FCFS ---")
print("Seek sequence:", fcfs_seq)
print("Total seek time:", fcfs_seek)

direction = input("\nEnter direction for SCAN (left/right): ").lower()
scan_seek, scan_seq = scan(requests, head, disk_size, direction)
print("\n--- SCAN ---")
print("Seek sequence:", scan_seq)
print("Total seek time:", scan_seek)

cscan_seek, cscan_seq = c_scan(requests, head, disk_size)
print("\n--- C-SCAN ---")
print("Seek sequence:", cscan_seq)
print("Total seek time:", cscan_seek)