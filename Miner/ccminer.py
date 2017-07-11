from Miner import Miner

class ccminer(Miner):
	def __init__(self, serverInformation, debug = False):
		super(ccminer, self).__init__(self.__class__.__name__, serverInformation, debug)

		self.setBinaryArguments('-a ###algorithm### -o stratum+tcp://###host###:###port### -O ###wallet###.###worker###:###password###')

	def stdOutEvent(self, line):
		print(__name__ + '> ' + line)