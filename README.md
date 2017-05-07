You should write a program that simulates some aspects of operating systems. There is no real system programming involved. The whole simulation is based on text inputs that the program receives from user.
 
 
# Scheduling

Your program should use the following multilevel scheduling. There are 5 priority levels numbered from 0 to 4. 0 is the lowest priority and 4 is the highest. There are 5 levels in the ready-queue, one for each priority level. Within each level of the ready-queue the FCFS algorithm is used. A process from some level of the ready-queue can be scheduled only if all higher levels are empty. The scheduling is preemptive: When a higher priority process becomes available for execution the lower priority process should be preemptied and sent to the end of its level of the ready queue.
 
 
All I/O-queues are FCFS.
 
 
# Memory

Your program should simulate contiguous memory allocation with “First-Fit” approach.
 
 
At the start, your program asks the user three questions:


* How much RAM memory is there on the simulated computer? Your program receives the number in bytes (no kilobytes or words). I can enter any number up to 4000000000 (4 billions).


* How many hard disks the simulated computer has? Enumeration of hard disks starts with 0.


* How many printers the simulated computer has? Enumeration of printers starts with 0.
 
 
After these questions are answered, the simulation begins. You program constantly listens for the user inputs. The user inputs signal some system events. Your program simulates the corresponding system behavior. The possible inputs are:
 
 
__A priority size__        ‘A’ input means that a new process has been created. This process has the priority priority and needs size bytes of RAM memory. For example, the input A 2 2000000 means that a new process has arrived. This process has the priority of 2 and needs 2000000 bytes to operate.

When a new process arrives, your program should create its PCB and allocate memory for it. If there is no memory for this process your program should print an error message and refuse to create the new process.

Also, when a new process is created your program should send it to the ready-queue or allow it to use the CPU right away.
When choosing PID for a new process start from 1 and go up. Do NOT reuse PIDs of the terminated processes.
 
 
__t__         The process that currently uses the CPU terminates. It leaves the system immediately. Make sure you release the memory used by this process. If the process was positioned in RAM next to a hole, make sure its RAM is merged with the hole. In other words, make sure there are no adjacent holes.
 
 
__d number__    The process that currently uses the CPU requests the hard disk #number.
 
 
__p number__    The process that currently uses the CPU requests the printer #number.
 
 
__D number__   The hard disk #number has finished the work for one process.
 
 
__P number__    The printer #number has finished the work for one process.
 
 
__S r__     Shows what process is currently using the CPU and what processes are waiting to use the CPU on each level of the ready-queue. Processes on the same level of the ready-queue should be listed in the order in which they are positioned in the queue.
 
 
__S i__      Shows what processes are currently using the I/O devices and what processes are waiting to use them. For each busy device show the process that uses it and show its I/O-queue.
 
 
__S m__    Shows the state of memory. Display the range of addresses occupied by each process in the system.
