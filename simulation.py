from managers import *
from process import *
from processor import *
from scheduler import *

mem_size = 0
num_hdd = 0
num_printer = 0

#get user input
print("How much RAM Memory is there on the simulated computer?")
mem_size = input()
while(mem_size <= 0):
    print("Please print a valid size.")
    mem_size = input()

print("How many hard disks the simulated computer has?")
num_hdd = input()
while(num_hdd <= 0):
    print("Please print a valid size.")
    mem_size = input()


print("How many printers the simulated computer has?")
num_printer = input()
while(num_printer <= 0):
    print("Please print a valid size.")
    mem_size = input()

print('Your simulated computer has {} bytes of RAM,  {} HDD(s),  {} Printer(s).'.format(mem_size, num_hdd, num_printer))

#computer components
cpu = CPU()
sched = Scheduler()
mem_manager = MemoryManager(mem_size)
hd_manager = HardDriveManager(num_hdd)
printer_manager = PrinterManager(num_printer)

user_input = ''
