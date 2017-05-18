class Process: 

    p_id = 1

    def __init__(self, priority, size):
        self.id = Process.p_id
        Process.p_id += 1
        self.priority = priority
        self.size = size
        
