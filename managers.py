from process import Process

class MemoryManager():

    pid_counter = 0

    def __init__(self, size):
        self.size = size
        self.pcb_map = {}
        inital_hole = FreeMemorySlot(size)
        self.memory = [inital_hole]

    def put(self, process):
        success = False
        for i in range(len(self.memory)):
            if(self.memory[i].free):
                if(process.size <= self.memory[i].size):
                    #insert at the front of the slot and reduce slot size
                    p = UsedMemorySlot(process)
                    self.memory[i].size = self.memory[i].size - p.size
                    if(self.memory[i].size == 0):
                        self.memory.pop(i)
                        self.memory = self.memory[:i-1] + [p] + self.memory[i:]
                    else:
                        self.memory = self.memory[:i] + [p] + self.memory[i:]
                    success = True
                    break
        return success
    
    def snapshot(self):
        start = 0
        counter = 0
        for i in range(len(self.memory)):
            print('Process {}: {} {}'.format(counter,start,start+self.memory[i].size))
            start += self.memory[i].size
            counter+=1


class FreeMemorySlot():

    def __init__(self, s):
        self.size = s
        self.free = True

class UsedMemorySlot(FreeMemorySlot):

    def __init__(self, p):
        FreeMemorySlot.__init__(self,p.size)
        self.free = False
        self.process = p

class PCB():

    def __init__(self):
        self.pid = 0
        self.starting_addr = 0
        self.state = None

class HardDriveManager():
    
    def __init__(self, size):
        self.size = size

class PrinterManager():
    
    def __init__(self, size):
        self.size = size
