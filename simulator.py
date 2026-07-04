from process import process
from collections import deque 
import copy


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


def sjf(processes):
    processes.sort(key = lambda p: p.arrival_time)
    n = len(processes)
    completed = 0 
    current_time = 0
    is_done = [False] * n

    while completed < n :
        # Find all processes that have arrived and aren't done yet
        available = []
        for idx in range(n):
            if not is_done[idx] and processes[idx].arrival_time <= current_time:
                available.append(idx)

        if not available :
            # nobody ready yet , jump clock to next arrival 
            next_arrival = min(processes[idx].arrival_time for idx in range(n) if not is_done[idx])
            current_time = next_arrival
            continue

        #pick the available process with smallest burst time 

        idx = min(available, key = lambda i: processes[i].burst_time)
        p = processes[idx]

        p.start_time = current_time
        current_time += p.burst_time
        p.completion_time = current_time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.start_time - p.arrival_time

        is_done[idx] = True

        completed += 1

    return processes


def priority_scheduling(processes):
    processes.sort(key = lambda p: p.arrival_time)
    n = len(processes)
    completed = 0
    current_time = 0 
    is_done = [False] * n

    while completed < n :
        available = []
        for idx in range(n):
            if not is_done[idx] and processes[idx].arrival_time <= current_time:
                available.append(idx)

        if not available:
            next_arrival = min(processes[idx].arrival_time for idx in range(n)if not is_done[idx])
            current_time = next_arrival
            continue

        # picks up the available process with lowest priority number as lower proiority number = higher priority 

        idx = min(available,key= lambda i : processes[i].priority)
        p = processes[idx]
        p.start_time = current_time

        current_time += p.burst_time
        p.completion_time = current_time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.waiting_time = p.start_time - p.arrival_time

        is_done[idx] = True

        completed +=1 

    return processes


def mlfq(processes , quantums = [2,4,8]):
    processes.sort(key = lambda p: p.arrival_time)
    n = len(processes)
    num_queues = len(quantums)
    queue = [deque() for _ in range(num_queues)] # queues = [deque(), deque(), deque()]

    current_time = 0 
    i = 0 # index itno processes , tracks who has arrived 
    completed = 0
    while completed < n:
        # add any newely arrived process into queue 0 
        while i < n and processes[i].arrival_time <= current_time:
            queue[0].append(processes[i])
            i += 1 


        #find the highest prirotiy non empty non empty queue 
        current_queue = None

        for q_level in range(num_queues):
            if queue[q_level] :
                current_queue = q_level
                break

        if current_queue is None:
            #nobody ready yet , jump clock to next arrival 
            current_time = processes[i].arrival_time
            continue


        #run the process of the first queue 

        p = queue[current_queue].popleft()

        if p.start_time is None:
            p.start_time = current_time 

        quantum = quantums[current_queue]
        run_time = min(quantum,p.remaining_time)
        current_time += run_time 
        p.remaining_time -= run_time

        # checking for new arrivals 
        while i < n and processes[i].arrival_time <= current_time:
            queue[0].append(processes[i])
            i+=1 

        if p.remaining_time == 0:
            p.completion_time = current_time 
            p.turnaround_time = p.completion_time - p.arrival_time
            p.waiting_time = p.turnaround_time - p.burst_time
            completed += 1 

        else :
            #demotion
            next_queue = min(current_queue + 1 , num_queues-1)
            queue[next_queue].append(p)


    return processes 


def cfs(processes, time_slice = 1 ):
    processes.sort(key = lambda p : p.arrival_time)
    n = len(processes)
    completed = 0 
    current_time = 0

    # assigning each process a vruntime , starting at 0 

    for p in processes :
        p.vruntime = 0 

    while completed < n :
        # each process in ready queue but not executed yet 
        available = [p for p in processes if p.arrival_time <= current_time and p.remaining_time > 0]

        if not available:
            # if no process is arrived yet 
            not_arrived = [p for p in processes if p.remaining_time> 0 ]
            current_time = min(p.arrival_time for p in not_arrived)
            continue 


        # pick the process with lowest vruntime 

        p = min(available, key = lambda proc: proc.vruntime)


        if p.start_time is None:
            p.start_time = current_time 

        run_time = min(time_slice, p.remaining_time)
        current_time += run_time 
        p.remaining_time -= run_time
        p.vruntime += run_time

        if p.remaining_time == 0 :
            p.completion_time = current_time
            p.turnaround_time = p.completion_time - p.arrival_time
            p.waiting_time = p.turnaround_time - p.burst_time
            completed += 1 

    return processes 


def calculate_averages(processes):
    n = len(processes)
    avg_waiting = sum(p.waiting_time for p in processes)/n
    avg_turnaround = sum(p.turnaround_time for p in processes)/n
    return avg_turnaround, avg_waiting

















