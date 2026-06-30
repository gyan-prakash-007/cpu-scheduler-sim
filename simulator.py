from process import process

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