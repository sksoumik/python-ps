"""
Given n processes with their burst times, the task is to find average waiting
time and average turn around time using FCFS scheduling algorithm.
Assume, arrival time for all processes is 0.

Completion Time: Time at which process completes its execution.

Turn Around Time: Time Difference between completion time and arrival time.
Turn Around Time = Completion Time – Arrival Time

Waiting Time(W.T): Time Difference between turn around time and burst time.
Waiting Time = Turn Around Time – Burst Time

As, we have assumed arrival times as 0, so turn around and completion times are same.

Algorithm:

1-  Input the processes along with their burst time (burst_time).
2-  Find waiting time (waiting_time) for all processes.
3-  As first process that comes need not to wait so
    waiting time for process 1 will be 0 i.e. waiting_time[0] = 0.
4-  Find waiting time for all other processes i.e. for
     process i ->
       waiting_time[i] = burst_time[i-1] + waiting_time[i-1] .
5-  Find turnaround time = waiting_time + burst_time
    for all processes.
6-  Find average waiting time =
                 total_waiting_time / no_of_processes.
7-  Similarly, find average turnaround time =
                 total_turn_around_time / no_of_processes.
"""


def find_waiting_time(processes, length, burst_time, waiting_time):
    # waiting time for the first process is 0
    waiting_time[0] = 0

    # calculating waiting time
    for i in range(1, length):
        waiting_time[i] = burst_time[i - 1] + waiting_time[i - 1]


def find_turn_around_time(processes, n, burst_time, waiting_time,
                          turn_around_time):
    # calculating turnaround time by adding burst_time[i] + waiting_time[i]
    for i in range(n):
        turn_around_time[i] = burst_time[i] + waiting_time[i]


def find_avg_time(processes, length, burst_time):
    waiting_time = [0] * length
    turn_around_time = [0] * length
    total_wt = 0
    total_tat = 0

    # Function to find waiting time of all processes
    find_waiting_time(processes, length, burst_time, waiting_time)

    # Function to find turn around time for all processes
    find_turn_around_time(processes, length, burst_time, waiting_time,
                          turn_around_time)

    # Display processes along with all details
    print("Processes " + "\tBurst time" + "\tWaiting time" +
          "\tTurn around time")

    # Calculate total waiting time and total turn around time
    for i in range(length):
        total_wt = total_wt + waiting_time[i]
        total_tat = total_tat + turn_around_time[i]
        print(" " + str(i + 1) + "\t\t\t" + str(burst_time[i]) + "\t\t\t " +
              str(waiting_time[i]) + "\t\t\t\t " + str(turn_around_time[i]))

    print("Average waiting time = " + str(total_wt / length))
    print("Average turn around time = " + str(total_tat / length))


if __name__ == '__main__':
    processes = [1, 2, 3]
    length = len(processes)
    burst_time = [10, 5, 8]

    find_avg_time(processes, length, burst_time)
