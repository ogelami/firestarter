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

x = minerHandler.getMiner('docker_cpuminer_opt')(config.miner['docker_cpuminer_opt'], 'cryptonight', config.pools['nicehash']['cryptonight'])
x.start()

#k = ccminer(1,2,3,4)

#print(1)
