import config
from time import sleep
from threading import Thread
from InputHandler import InputHandler
from IdleHandler import IdleHandler
from Miner import Miner

class Firestarter(object):
  def __init__(self):
    super(Firestarter, self).__init__()

    self.miner = {}

    self.shutdown = False
    self.idlePause = False

    self.idleHandler = IdleHandler(self.onIdle, self.onActive)
    self.inputHandler = InputHandler(self.inputLogic)

    self.inputHandler.bind('q', 'shutdown')

    self.inputHandler.bind('g', 'spawn-nicehash-daggerhashimoto')
    self.inputHandler.bind('c', 'spawn-nicehash-cryptonight')
    self.inputHandler.bind('t', 'spawn-nicehash-lyra2rev2')
    self.inputHandler.bind('a', 'spawn-nicehash-equihash')

    self.inputHandler.bind('h', 'dump-nicehash-daggerhashimoto')
    self.inputHandler.bind('v', 'dump-nicehash-cryptonight')
    self.inputHandler.bind('y', 'dump-nicehash-lyra2rev2')
    self.inputHandler.bind('s', 'dump-nicehash-equihash')

    self.inputHandler.bind('j', 'terminate-nicehash-daggerhashimoto')
    self.inputHandler.bind('b', 'terminate-nicehash-cryptonight')
    self.inputHandler.bind('u', 'terminate-nicehash-lyra2rev2')
    self.inputHandler.bind('d', 'terminate-nicehash-equihash')

    self.inputHandler.bind('i', 'idlePause')

#    self.inputHandler.bind('g', self.tryStart('nicehash-daggerhashimoto'))
#    self.inputHandler.bind('h', self.miner['nicehash-daggerhashimoto'].dump)

#    self.inputHandler.bind('c', self.tryStart('ob-test'))
#    self.inputHandler.bind('v', self.miner['ob-test'].dump)

    self.inputHandler.start()
    self.idleHandler.start()

  #when user became inactive
  def onIdle(self):
    if not self.idlePause:
      self.inputLogic('spawn-nicehash-equihash')
      self.inputLogic('spawn-nicehash-cryptonight')

  #when user became active
  def onActive(self):
    if not self.idlePause:
      self.inputLogic('terminate-nicehash-equihash')
      self.inputLogic('terminate-nicehash-cryptonight')

  def inputLogic(self, inputFunction):
    if inputFunction == 'shutdown':
      self.shutdownRequest()
    elif inputFunction.startswith('spawn-'):
      self.spawn(inputFunction[6:])
    elif inputFunction.startswith('dump-'):
      self.dump(inputFunction[5:])
    elif inputFunction.startswith('terminate-'):
      self.terminate(inputFunction[10:])
    elif inputFunction == 'idlePause':
      self.idlePause = not self.idlePause
      print('idlePause = %d' % self.idlePause)

  def dump(self, miner):
    if miner in self.miner:
      self.miner[miner].dump()

  def terminate(self, miner):
    if miner in self.miner:
      self.miner[miner].shutdown()

  def spawn(self, miner):
    if miner in config.pools:
      if miner in self.miner and self.miner[miner].isRunning:
        print('Thread is already running!')
      else:
        self.miner[miner] = Miner(config.pools[miner])
        self.miner[miner].start()
    else:
      print("%s not in config.pools" % miner)

  def shutdownRequest(self):
    print('Shutting down.')

    runningMiners = -1

    while runningMiners != 0:
      runningMiners = 0

      for miner in self.miner:
        if self.miner[miner].isRunning:
          self.miner[miner].shutdown()
          runningMiners += 1

    self.shutdown = True

  def start(self):
    while not self.shutdown:
      sleep(1)