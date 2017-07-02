from threading import Thread
from queue import Queue
import subprocess, sys, config

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
#    print("%s %s" % (self.binaryPath, self.binaryArguments))
    self.isRunning = True
    stdout = sys.stdout if self.debug else subprocess.PIPE
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

class PartyPiper(Thread):
  """PartyPiper is a thread enqueue/dequeue stdout from process"""
  def __init__(self, inputStream, maxQueueLength = config.stdOutBufferRows):
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