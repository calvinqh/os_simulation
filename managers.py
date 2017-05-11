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
                if(process.size < self.memory[i].size):
                    #insert at the front of the slot and reduce slot size
                    p = UsedMemorySlot(p)
                    self.memory[i].size = self.memory[i].size - p.size
                    if(self.memory[i].size == 0):
                        self.memory.pop(i)
                        self.memory = self.memory[:i] + p + self.memory[i:]
                    else:
                        self.memory = self.memory[:i] + p + self.memory[i:]
                    success = True
                    break
        return success


class Slot():
    
    size = 0
    free= False

    def __init__(self, s, f):
        size = s
        free = f

class FreeMemorySlot(Slot):

    def __init__(self, size=0):
        Slot.__init__(self,size,True)

class UsedMemorySlot(Slot):


    def __init__(self, p):
        Slot.__init__(self,p.size,False)
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

