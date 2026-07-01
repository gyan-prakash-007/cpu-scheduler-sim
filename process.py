class process:
    def __init__(self,pid,arrival_time,burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.start_time = None
        self.completion_time = None
        self.waiting_time = 0
        self.turnaround_time = 0



if __name__ == "__main__":
    p1 = process(1,0,5)
    print(p1.pid)
    print(p1.arrival_time)
    print(p1.burst_time)