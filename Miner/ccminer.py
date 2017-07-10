from Miner import Miner

class ccminer(Miner):
	def __init__(self, minerConfig, serverInformation):
		super(docker_cpuminer_opt, self).__init__(minerConfig, serverInformation)

	def stdOutEvent(self, line):
		print(__name__ + '> ' + line)