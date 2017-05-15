class CPU:
    
    def __init__(self):
        self.running_process = None

    def run(self, process):
        if(self.running_process != None):
            print("Error: There is currently a running process. Must terminate process first.")
        self.running_process = process

    def terminate(self):
        t = self.running_process
        self.running_process = None
        return t

    def isBusy(self):
        return self.running_process != None

    def check_priority(self):
        if self.running_process != None:
            return self.running_process.priority
        return None
