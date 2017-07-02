import config
from ctypes import Structure, windll, c_uint, sizeof, byref
from time import sleep
from threading import Thread
import subprocess
import sys
import msvcrt
from queue import Queue

class InputHandler(Thread):
  def __init__(self, inputLogicFunction):
    super(InputHandler, self).__init__()
    self.daemon = True
    self.bindList = {}
    self.inputLogicFunction = inputLogicFunction

  def bind(self, key, functionName):
    print("Bound %s to %s" % (key, functionName))
    self.bindList[key] = functionName

  def run(self):
    print("%s Started." % __class__.__name__)

    while True:
      char = msvcrt.getch().decode('utf8')

      if char in self.bindList:
        self.inputLogicFunction(self.bindList[char])
      else:
        print("Keypress %s" % char)

class Firestarter(object):
  def __init__(self):
    super(Firestarter, self).__init__()

    self.miner = {}

    self.shutdown = False
    self.idle = False

    self.inputHandler = InputHandler(self.inputLogic)

    self.inputHandler.bind('q', 'shutdown')

    self.inputHandler.bind('g', 'spawn-nicehash-daggerhashimoto')
    self.inputHandler.bind('c', 'spawn-nicehash-cryptonight')

    self.inputHandler.bind('h', 'dump-nicehash-daggerhashimoto')
    self.inputHandler.bind('v', 'dump-nicehash-cryptonight')

    self.inputHandler.bind('j', 'terminate-nicehash-daggerhashimoto')
    self.inputHandler.bind('b', 'terminate-nicehash-cryptonight')

#    self.inputHandler.bind('g', self.tryStart('nicehash-daggerhashimoto'))
#    self.inputHandler.bind('h', self.miner['nicehash-daggerhashimoto'].dump)

#    self.inputHandler.bind('c', self.tryStart('ob-test'))
#    self.inputHandler.bind('v', self.miner['ob-test'].dump)

    self.inputHandler.start()

  def inputLogic(self, inputFunction):
    if inputFunction == 'shutdown':
      self.shutdownRequest()
    elif inputFunction.startswith('spawn-'):
      self.spawn(inputFunction[6:])
    elif inputFunction.startswith('dump-'):
      self.dump(inputFunction[5:])
    elif inputFunction.startswith('terminate-'):
      self.terminate(inputFunction[10:])

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
  
  def getIdleTimeTriggered(self, maxIdleTime):
      lastInputInfo = self.LASTINPUTINFO()
      lastInputInfo.cbSize = sizeof(lastInputInfo)
      windll.user32.GetLastInputInfo(byref(lastInputInfo))
      currentIdleTime = (windll.kernel32.GetTickCount() - lastInputInfo.dwTime) / 1000.0

      return currentIdleTime > maxIdleTime

  def start(self):
    while not self.shutdown:
      if self.getIdleTimeTriggered(config.maxIdleTime):
        if not self.idle:
          self.spawn('nicehash-daggerhashimoto')
          self.spawn('nicehash-cryptonight')
        self.idle = True
      else:
        if self.idle:
          self.terminate('nicehash-daggerhashimoto')
          self.terminate('nicehash-cryptonight')
        self.idle = False


      sleep(1)

  class LASTINPUTINFO(Structure):
    _fields_ = [
      ('cbSize', c_uint),
      ('dwTime', c_uint),
    ]

class PartyPiper(Thread):
  """PartyPiper is a thread that move keeps a queue of stdout"""
  def __init__(self, inputStream, maxQueueLength = 10):
    super(PartyPiper, self).__init__()
    self.daemon = False
    self.input = inputStream
    self.queue = Queue()
    self.maxQueueLength = maxQueueLength

  def run(self):
    for line in self.input:
      if self.queue.qsize() > self.maxQueueLength:
        self.queue.get(False)

      self.queue.put(line)

    print('Piper down.')

  def dump(self):
    while not self.queue.empty():
      print(self.queue.get(), end = '')

class Miner(Thread):
  def __init__(self, arguments, debug = False):
    super(Miner, self).__init__()
    self.daemon = False
    self.debug = debug
    self.isRunning = False

    self.minerName = arguments['minerName']
    self.binaryPath = arguments['binaryPath']
    self.binaryArguments = arguments['arguments']
    self.stdOutQueue = Queue()

    self.binaryArguments = self.binaryArguments.replace('###host###', arguments['host']).replace('###port###', arguments['port']).replace('###wallet###', config.wallet).replace('###worker###', config.worker).replace('###password###', arguments['password'])

  def stdOutEnqueue(self, stdIn):
    print("%s thread spawned." % __name__)

    for line in stdIn:
      self.stdOutQueue.put(line)

  def run(self):
    self.isRunning = True

    stdout = sys.stdout if self.debug else subprocess.PIPE
    print("%s %s" % (self.binaryPath, self.binaryArguments))

    self.process = subprocess.Popen([self.binaryPath] + self.binaryArguments.split(' '), stdout=stdout, bufsize=1, stderr=subprocess.STDOUT, universal_newlines=True)
    
    if stdout == subprocess.PIPE:
      self.partyPiper = PartyPiper(self.process.stdout)
      self.partyPiper.start()

    print("Starting %s." % self.minerName)

  def shutdown(self):
    self.process.stdout.close()
    self.process.terminate()
    self.process.wait()
   
    self.isRunning = False
    print("Miner down.")
    # need to kill the partyPiper, its likely locked here.

  def dump(self):
    if not self.isRunning:
      print('Thread not running!')
      return False

    if not hasattr(self, 'partyPiper'):
      print('dump() only available when miner is not in debugging mode.')
      return False

    self.partyPiper.dump()

f = Firestarter()
f.start()

#daggerhashimoto.eu.nicehash.com
#3353
#1ChM1MDWwH2F58F923oq3e8bVKpFtTVS3L

#f = Firestarter()
#f.start()

#print(ctypes.windll.user32)
#GetLastInputInfo = ctypes.windll.user32.GetLastInputInfo
#r = GetLastInputInfo(x)

#sleep(2)

#print(r)
#print(x)
#"--cuda -S daggerhashimoto.eu.nicehash.com:3353 -O 1ChM1MDWwH2F58F923oq3e8bVKpFtTVS3L.modermodemet:x --api-port 4001 --cuda-devices 0 --dag-load-mode singlekeep 0"0