#!/usr/bin/env python3

#from Firestarter import Firestarter
#firestarter = Firestarter()
#firestarter.start()


#from IdleHandler import IdleHandler
#ih = IdleHandler()
#ih.start()

#from time import sleep

#while True:
#  sleep(1)

#from Miner import Ccminer
#from Miner import Miner
from threading import Thread
#from Miner import ccminer
from Miner import *
import config
from time import sleep

m = minerHandler.getMiner('docker_cpuminer_opt')(config.miner['docker_cpuminer_opt'], config.pools['nicehash']['cryptonight'])
m.setAlgorithm('cryptonight')
#m.start()
#sleep(5)
print('shutting down')
#m.shutdown()
#print('sleeping 5')
#sleep(5)
print('done')

#k = ccminer(1,2,3,4)

#print(1)
