from threading import Thread
from queue import Queue
import subprocess, sys, signal, config
from os.path import dirname, basename, isfile
from glob import glob
import os

class Miner(Thread):
  def __init__(self, minerConfig, serverInformation, debug = False):
    super(Miner, self).__init__()
    self.daemon = False
    self.isRunning = False
    self.binaryArguments = False
    self.debug = debug
    self.minerConfig = minerConfig
    self.serverInformation = serverInformation

  def setBinaryArguments(self, argumentQuery):
    self.binaryArguments = argumentQuery

  def reportSpeed(self):
    raise NotImplementedError

  #abstract method should be implemented in child class
  def stdOutEvent(self, line):
    raise NotImplementedError

  def setAlgorithm(self, algorithm):
    if not algorithm in self.minerConfig['algorithmSupport']:
      print('I do not support the %s algorithm.' % algorithm)
      return False

    self.algorithm = algorithm
    return True

  def setHardware(self, hardware):
    if not algorithm in self.minerConfig['algorithmSupport']:
      print('I do not support mining with %s.' % hardware)

    self.hardware = hardware

  def run(self):
    if not self.binaryArguments:
      print('Missing binary arguments for miner.')
      return False

    self.binaryArguments = self.binaryArguments.replace('###host###', self.serverInformation['host']).replace('###port###', self.serverInformation['port']).replace('###wallet###', config.wallet).replace('###worker###', config.worker).replace('###password###', self.serverInformation['password']).replace('###username###', self.serverInformation['username']).replace('###algorithm###', self.algorithm)
    self.isRunning = True

    stdout = sys.stdout if self.debug else subprocess.PIPE
    execute = [self.minerConfig['binaryPath']] + self.binaryArguments.split(' ')

    self.process = subprocess.Popen(execute, stdout=stdout, bufsize=1, stderr=subprocess.STDOUT, universal_newlines=True, preexec_fn=os.setsid)
    
    if stdout == subprocess.PIPE:
      self.processQueuerThread = Thread(target=self.stdQueuer, args=(self.process.stdout, self.stdOutEvent), daemon = True)
      self.processQueuerThread.start()

  #should always be threaded
  def stdQueuer(self, stdout, eventTrigger):
    try:
      for line in stdout:
        eventTrigger(line.strip())
    except ValueError as e:
      print(__name__ + ' closing')
    except Exception as e:
      print('error')
      print(e)
      print(k)
    finally:
      stdout.close()

  def shutdown(self):
#    self.process.stdout.close()
    print('calling terminate')
    os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
    print(os.kill(self.process.pid, signal.SIGTERM))
    self.process.kill()
    print('waiting for proc close.')
    self.process.wait()
   
    self.isRunning = False
    print("Miner down.")
    # need to kill the partyPiper, its likely locked here.

#  def dump(self):
#    if not self.isRunning:
#      print('Thread not running!')
#      return False
#
#    if not hasattr(self, 'partyPiper'):
#      print('dump() only available when miner is not in debugging mode.')
#      return False
#
#    self.partyPiper.dump()

#class PartyPiper(Thread):
#  """PartyPiper is a thread enqueue/dequeue stdout from process"""
#  def __init__(self, inputStream, maxQueueLength = config.stdOutBufferRows):
#    super(PartyPiper, self).__init__()
#    self.daemon = False
#    self.input = inputStream
#    self.queue = Queue()
#    self.maxQueueLength = maxQueueLength
#
#  def run(self):
#    for line in self.input:
#      if self.queue.qsize() > self.maxQueueLength:
#        self.queue.get(False)
#      self.queue.put(line)
#    print('Piper down.')
#
#  def dump(self):
#    while not self.queue.empty():
#      print(self.queue.get(), end = '')

class MinerHandler(object):
  def __init__(self):
    self.minerClassDictionary = {}

    modules = glob(dirname(__file__) + "/*.py")

    for module in modules:
      moduleName = basename(module)[:-3]
      if not moduleName == '__init__':
        module = __import__('%s.%s' % (__package__, moduleName), fromlist=[moduleName])
        self.minerClassDictionary[moduleName] = getattr(module, moduleName)

  def getMiner(self, miner):
    return self.minerClassDictionary[miner]

global minerHandler
minerHandler = MinerHandler()
