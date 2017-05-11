import re

class Util:
    new_process = re.compile('A \d+ \d+')
    terminate = re.compile('t')
    disk_request = re.compile('d \d+')
    disk_complete = re.compile('p \d+')
    print_request = re.compile('D \d+')
    print_complete = re.compile('P \d+')
    show_ready = re.compile('S r')
    show_io_ready = re.compile('S i')
    show_memory = re.compile('S m')
    
    def isValid(self, commor):
        valid = True
        if self.new_process.match(commor)!=None or self.terminate.match(commor)!=None or self.disk_request.match(commor)!=None:
            return valid
        if self.disk_complete.match(commor)!=None or self.print_request.match(commor)!=None:
            return valid
        if self.print_complete.match(commor)!=None or self.show_ready.match(commor)!=None:
            return valid
        if self.show_io_ready.match(commor)!=None or self.show_memory.match(commor)!=None:
            return valid
        return False
