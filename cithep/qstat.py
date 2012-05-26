from subprocess import check_output
from os import getlogin
class qline:
	def __init__(self,line):
		qtoken = line.split()
		self.jobid = qtoken[0]
		self.jname = qtoken[1]
		self.qtime = qtoken[2]
		self.jstatus = qtoken[3]
		self.jque = qtoken[4]
		
def qstat():
	qout = check_output('qstat')[1:]
	ret = []
	for line in qout:
		ret.append(qline(line))
	return ret
			
print qstat()
