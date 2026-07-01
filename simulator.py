from process import process
from collections import deque 


def fcfs(process):
    #sort process by arrival time // first come first serve 
    process.sort(key=lambda p: p.arrival_time)

    current_time = 0

    for p in process:
        if current_time < p.arrival_time:
            current_time = p.arrival_time

        p.start_time = current_time
        current_time += p.burst_time 
        p.completion_time = current_time 

        p.turnaround_time = p.completion_time - p.arrival_time 
        p.waiting_time = p.start_time - p.arrival_time 

    return process 



def  round_robin(processes, quantum):
    processes.sort(key =lambda p: p.arrival_time)
    queue = deque()
    current_time = 0
    i = 0 # index tp track which processes have arrived
    n = len(processes)
    completed = 0

    while completed < n :
        # Add any process that have arrived by current_time into the queue 
        while i < n and processes[i].arrival_time <= current_time:
            queue.append(processes[i])
            i += 1

        if not queue :
            #no process ready yet , jump to next arrival time 
            current_time = processes[i].arrival_time
            continue

        p = queue.popleft()

        if p.start_time is None:
            p.start_time = current_time

        run_time = min(quantum, p.remaining_time)
        current_time += run_time 
        p.remaining_time -= run_time

        while i < n and processes[i].arrival_time <= current_time:
            queue.append(processes[i])
            i += 1 

        if p.remaining_time > 0 :
            queue.append(p)

        else:
            p.completion_time = current_time
            p.turnaround_time = p.completion_time - p.arrival_time
            p.waiting_time = p.turnaround_time - p.burst_time
            completed += 1 

    return processes






