from subprocess import check_output
class Job:
    def __init__(self,line):
        qtoken = line.split()
        self.jobid = qtoken[0]
        self.jname = qtoken[1]
        self.owner = qtoken[2]
        self.qtime = qtoken[3]
        self.status = qtoken[4]
        self.jque = qtoken[5]
    
def qstat():
    qout = check_output('qstat').split('\n')[2:-1]
    ret = []
    for line in qout:
        ret.append(Job(line))
    return ret

