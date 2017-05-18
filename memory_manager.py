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
                    self.pcb_map[process.id]=process
                    self.memory[i].size = self.memory[i].size - p.size
                    if(self.memory[i].size == 0):
                        self.memory.pop(i)
                        self.memory = self.memory[:i] + [p] + self.memory[i:]
                    else:
                        self.memory = self.memory[:i] + [p] + self.memory[i:]
                    success = True
                    break
        return success

    def release(self, process):
        for i in range(len(self.memory)):
            if(not self.memory[i].free and process.id == self.memory[i].process.id):
                #clear it
                free_slot = FreeMemorySlot(process.size)
                self.memory = self.memory[:i] + [free_slot] + self.memory[i+1:]
                if(i-1>=0 and i+1<len(self.memory) and self.memory[i-1].free and self.memory[i+1].free):
                    #merge left and right
                    fs = FreeMemorySlot(process.size+self.memory[i-1].size+self.memory[i+1].size)
                    self.memory = self.memory[:i-1] + [fs] + self.memory[i+2:]
                elif(i-1>=0 and self.memory[i-1].free):
                    #merge left
                    fs = FreeMemorySlot(process.size+self.memory[i-1].size)
                    self.memory = self.memory[:i-1] + [fs] + self.memory[i+1:]
                elif(i+1<len(self.memory) and self.memory[i+1].free):
                    #merge right
                    fs = FreeMemorySlot(process.size+self.memory[i+1].size)
                    self.memory = self.memory[:i] + [fs] + self.memory[i+2:]
                break;
        print("Process has been released.")
    
    def snapshot(self):
        start = 0
        counter = 0
        for i in range(len(self.memory)):
            if(self.memory[i].free):
                print('Free Memory: {} {}'.format(start,start+self.memory[i].size-1))
                start += self.memory[i].size
            else:
                print('Process {}: {} {}'.format(self.memory[i].process.id,start,start+self.memory[i].size-1))
                start += self.memory[i].size


class FreeMemorySlot():

    def __init__(self, s):
        self.size = s
        self.free = True

class UsedMemorySlot(FreeMemorySlot):

    def __init__(self, p):
        FreeMemorySlot.__init__(self,p.size)
        self.free = False
        self.process = p


