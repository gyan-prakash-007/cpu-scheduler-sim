from process import process
from simulator import fcfs

p1 = process(1,0,5)
p2 = process(2,1,3)
p3 = process(3,2,8)

processes = [p1,p2,p3]

result = fcfs(processes)

for p in result:
    print(f"P{p.pid}: start={p.start_time} , completion={p.completion_time}, "
          f"waiting={p.waiting_time}, turnaround={p.turnaround_time} ")