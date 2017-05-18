import queue

class HardDriveManager():
    
    def __init__(self, size):
        self.size = size
        self.running_process = [None for i in range(size+1)]
        self.wait_list = [queue.Queue() for i in range(size+1)]
    
    def put(self, hd_id, process):
        if(self.running_process[hd_id] == None):
            self.running_process[hd_id] = process
        else:
            self.wait_list[hd_id].put(process)

    def complete(self, hd_id):
        if(self.running_process[hd_id] != None):
            t = self.running_process[hd_id]
            if(not self.wait_list[hd_id].empty()):
                self.running_process[hd_id] = self.wait_list[hd_id].get()
            else:
                self.running_process[hd_id] = None
            return t
        return None

    def snapshot(self):
        for i in range(self.size)[1:]:
            print('Hard Drive {} Running: {}'.format(i, self.stringify_for_hd_r(i)))
            print('Hard Drive {} Queue: {}'.format(i, self.stringify_for_hd_q(i)))

    def stringify_for_hd_r(self, hd_id):
        t = 'Empty'
        if(self.running_process[hd_id] != None):
            t = self.running_process[hd_id].id
        return t

    def stringify_for_hd_q(self, hd_id):
        temp = []
        result = ''
        while(not self.wait_list[hd_id].empty()):
            x = self.wait_list[hd_id].get()
            if(x is None):
                break
            temp.append(x)
            result = result + '  ' + str(x.id)
        for i in range(len(temp)):
            self.wait_list[hd_id].put(temp[i])
        return result
