from managers import *
from process import *
from processor import *
from scheduler import *
from utils import Util
import re


mem_size = 0
num_hdd = 0
num_printer = 0

#get user input
print("How much RAM Memory is there on the simulated computer?")
mem_size = int(input())
while(mem_size <= 0):
    print("Please print a valid size.")
    mem_size = input()

print("How many hard disks the simulated computer has?")
num_hdd = int(input())
while(num_hdd <= 0):
    print("Please print a valid size.")
    mem_size = input()


print("How many printers the simulated computer has?")
num_printer = int(input())
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
utils = Util()

user_input = ''

#wait for input
while(True):
    print("What would you like to do?")
    user_input = input()
    #verify inputs
    while(not utils.isValid(user_input)):
        print("Enter valid command!")
        user_input = input()
    #do command
    if(utils.new_process.match(user_input)):
        #parse the input, retrieve the priority and size, and create the new process
        variables = re.split('\W+',user_input)
        #check if there is enough space in memory
        #create process and pcb
        p = Process(int(variables[1]), int(variables[2]))
        suc = mem_manager.put(p)
        print(suc)
        #put it into cpu if 
        if(sched.peek_highest() == -1 and not cpu.isBusy()):
            cpu.run(p)
        else:
            print('Goes to the ready queue!')
            sched.put(p)
        
    if(utils.terminate.match(user_input)):
        pass
    if(utils.disk_request.match(user_input)):
        pass
    if(utils.disk_complete.match(user_input)):
        pass
    if(utils.print_request.match(user_input)):
        pass
    if(utils.print_complete.match(user_input)):
        pass
    if(utils.show_ready.match(user_input)):
        pass
    if(utils.show_io_ready.match(user_input)):
        pass
    if(utils.show_memory.match(user_input)):
        pass


