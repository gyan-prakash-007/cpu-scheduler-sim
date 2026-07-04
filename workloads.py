import random
from process import process 

def generate_workload(n , burst_range, arrival_spread , seed= None):
    if seed is not None :
        random.seed(seed)

    processes = []
    current_arrival = 0 
    for pid in range(1,n+1):
        current_arrival += random.randint(0,arrival_spread)
        burst = random.randint(burst_range[0],burst_range[1])
        processes.append(process(pid,current_arrival,burst))

    return processes


def cpu_heavy_workload(n = 10 , seed = 42 ):
    # long burst time 
    return generate_workload(n,burst_range=(10,20),arrival_spread=3,seed=seed)


def io_heavy_workload(n=10 ,seed=42):
    return generate_workload(n,burst_range=(1,4),arrival_spread=1,seed=seed)


def mix_workload(n=10, seed=42):
    processes = []
    for pid in range(1,n+1):
        if pid %2 ==0 :
            burst = random.randint(1,4)

        else:
            burst = random.randint(10,20)
        processes.append(process(pid,pid,burst))

    return processes

