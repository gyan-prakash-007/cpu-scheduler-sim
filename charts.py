import matplotlib.pyplot as plt
import copy
from workloads import cpu_heavy_workload, io_heavy_workload, mix_workload
from simulator import fcfs, round_robin, sjf, priority_scheduling, mlfq, cfs, calculate_averages

algorithms = {
    "FCFS": lambda procs: fcfs(procs),
    "Round Robin": lambda procs: round_robin(procs, quantum=2),
    "SJF": lambda procs: sjf(procs),
    "Priority": lambda procs: priority_scheduling(procs),
    "MLFQ": lambda procs: mlfq(procs, quantums=[2, 4, 8]),
    "CFS": lambda procs: cfs(procs),
}


def plot_workload(workload,workload_name):
    names = []
    avg_waits =[]

    for algo_name , algo_func in algorithms.items():
        procs_copy = copy.deepcopy(workload)
        result = algo_func(procs_copy)
        avg_wait, avg_turnaround = calculate_averages(result)
        names.append(algo_name)
        avg_waits.append(avg_wait)

    plt.figure(figsize=(8,5))
    plt.bar(names,avg_waits,color = "skyblue")
    plt.title(f"Average Waiting Time — {workload_name}")
    plt.xlabel("Algorithm")
    plt.ylabel("Average Waiting Time")
    plt.savefig(f"results_{workload_name}.png")
    plt.close()
    print(f"Saved chart: results_{workload_name}.png")
if __name__ == "__main__":
    plot_workload(cpu_heavy_workload(n=10), "CPU-heavy")
    plot_workload(cpu_heavy_workload(n=10), "CPU-heavy")
    plot_workload(io_heavy_workload(n=10), "IO-heavy")
    plot_workload(mix_workload(n=10), "Mixed")
