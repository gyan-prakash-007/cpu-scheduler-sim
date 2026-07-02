from process import process
from simulator import fcfs
from simulator import round_robin
from simulator import sjf
from simulator import priority_scheduling


p1 = process(1,0,5)
p2 = process(2,1,3)
p3 = process(3,2,8)

processes = [p1,p2,p3]

result = fcfs(processes)

print("\n--FCFS--")
for p in result:
    print(f"P{p.pid}: start={p.start_time} , completion={p.completion_time}, "
          f"waiting={p.waiting_time}, turnaround={p.turnaround_time} ")
    


p1 = process(1,0,5)
p2 = process(2,1,3)
p3 = process(3,2,8)

rr_processes = [p1,p2,p3]
rr_result = round_robin(rr_processes , quantum = 2)


print("\n -- Round Robin (Quantum = 2)--")
for p in rr_result:
    print(f"P{p.pid}: start={p.start_time}, completion={p.completion_time},"
          f"waiting={p.waiting_time}, turnaround= {p.turnaround_time}")
    

p1 = process(1, 0, 5)
p2 = process(2, 1, 3)
p3 = process(3, 2, 8)

sjf_processes = [p1,p2,p3]
sjf_result = sjf(sjf_processes)

print("n--SJF--")
for p in sjf_result:
    print(f"P{p.pid}: start ={p.start_time}, completion = {p.completion_time},"
          f"waiting= {p.waiting_time}, turnaround = {p.turnaround_time}")
    

p1 = process(1,0,5,priority=2)
p2 = process(2,1,3,priority=1)
p3 = process(3,2,8,priority=3)

pr_processes = [ p1,p2,p3]
pr_result = priority_scheduling(pr_processes)


print("\n--Priority Scheduling--")
for p in pr_result:
    print(f"P{p.pid}: start={p.start_time}, completion={p.completion_time}, "
          f"waiting={p.waiting_time}, turnaround={p.turnaround_time}")