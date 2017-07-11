from Miner import Miner

class docker_cpuminer_opt(Miner):
	def __init__(self, minerConfig, serverInformation, debug = False):
		super(docker_cpuminer_opt, self).__init__(self.__class__.__name__, serverInformation, debug)

		self.setBinaryArguments('run --net=host -p 50505:50505 hmage/cpuminer-opt -a ###algorithm### -o stratum+tcp://###host###:###port### -O ###wallet###.###worker###:###password###')

	def stdOutEvent(self, line):
		print(__name__ + '> ' + line)