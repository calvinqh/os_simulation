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
    
    def isValid(self, command):
        valid = True
        if new_process.match(command)!=None and terminate.match(command)!=None and disk_request.match(command)!=None:
            return valid
        if disk_complete.match(command)!=None and print_request.match(command)!=None:
            return valid
        if print_complete.match(command)!=None and show_ready.match(command)!=None:
            return valid
        if show_io_ready.match(command)!=None and show_memory.match(command)!=None:
            return valid
        return False
