from process import process
from simulator import fcfs
from simulator import round_robin
from simulator import sjf
from simulator import priority_scheduling
from simulator import mlfq
from simulator import cfs
from workloads import cpu_heavy_workload, io_heavy_workload, mix_workload
from simulator import calculate_average
import copy


# p1 = process(1,0,5)
# p2 = process(2,1,3)
# p3 = process(3,2,8)

# processes = [p1,p2,p3]

# result = fcfs(processes)

# print("\n--FCFS--")
# for p in result:
#     print(f"P{p.pid}: start={p.start_time} , completion={p.completion_time}, "
#           f"waiting={p.waiting_time}, turnaround={p.turnaround_time} ")
    


# p1 = process(1,0,5)
# p2 = process(2,1,3)
# p3 = process(3,2,8)

# rr_processes = [p1,p2,p3]
# rr_result = round_robin(rr_processes , quantum = 2)


# print("\n -- Round Robin (Quantum = 2)--")
# for p in rr_result:
#     print(f"P{p.pid}: start={p.start_time}, completion={p.completion_time},"
#           f"waiting={p.waiting_time}, turnaround= {p.turnaround_time}")
    

# p1 = process(1, 0, 5)
# p2 = process(2, 1, 3)
# p3 = process(3, 2, 8)

# sjf_processes = [p1,p2,p3]
# sjf_result = sjf(sjf_processes)

# print("n--SJF--")
# for p in sjf_result:
#     print(f"P{p.pid}: start ={p.start_time}, completion = {p.completion_time},"
#           f"waiting= {p.waiting_time}, turnaround = {p.turnaround_time}")
    

# p1 = process(1,0,5,priority=2)
# p2 = process(2,1,3,priority=1)
# p3 = process(3,2,8,priority=3)

# pr_processes = [ p1,p2,p3]
# pr_result = priority_scheduling(pr_processes)


# print("\n--Priority Scheduling--")
# for p in pr_result:
#     print(f"P{p.pid}: start={p.start_time}, completion={p.completion_time}, "
#           f"waiting={p.waiting_time}, turnaround={p.turnaround_time}")
    

# p1 = process(1,0,5,priority=2)
# p2 = process(2,1,3,priority=1)
# p3 = process(3,2,8,priority=3)

# mlfq_processes = [p1,p2,p3]
# mlfq_result = mlfq(mlfq_processes,quantums=[2,4,8])

# print("\n--- MLFQ ---")
# for p in mlfq_result:
#     print(f"P{p.pid}: start={p.start_time}, completion={p.completion_time}, "
#           f"waiting={p.waiting_time}, turnaround={p.turnaround_time}")
    

# p1 = process(1,0,5)
# p2 = process(2,1,3)
# p3 = process(3,2,8)

# cfs_processes = [p1,p2,p3]
# cfs_result = cfs(cfs_processes)
# print("\n--- CFS (simplified) ---")
# for p in cfs_result:
#     print(f"P{p.pid}: start={p.start_time}, completion={p.completion_time}, "
#           f"waiting={p.waiting_time}, turnaround={p.turnaround_time}")



print("\n -- Testing Workload Generator --")
cpu_proc = cpu_heavy_workload(n=5)
for p in cpu_proc:
    print(f"P{p.pid}: arrival={p.arrival_time}, burst={p.burst_time}")



workloads= {
    "cpu-heavy": cpu_heavy_workload(n=10),
    "I/O-Heavy": io_heavy_workload(n=10),
    "Mixed burst": mix_workload(n=10),

}

algorithms = {
    "FCFS" : lambda procs : fcfs(procs),
    "Round Robin": lambda procs: round_robin(procs, quantum=2),
    "SJF": lambda procs: sjf(procs),
    "Priority": lambda procs: priority_scheduling(procs),
    "MLFQ": lambda procs: mlfq(procs, quantums=[2, 4, 8]),
    "CFS": lambda procs: cfs(procs),
}

print("\n --Full Comparision--")
for workload_name , workload in workloads.items():
    print(f"\n WrorkLoad : {workload_name}")
    for algo_name , algo_func in algorithms.items():
        procs_copy = copy.deepcopy(workload)
        result = algo_func(procs_copy)
        avg_wait , avg_turnaround = calculate_average(result)
        print(f"  {algo_name}: avg_waiting={avg_wait:.2f}, avg_turnaround={avg_turnaround:.2f}")


