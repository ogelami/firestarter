from threading import Thread
import config
from time import sleep

class IdleHandler(Thread):
  def __init__(self, idleCallback, activeCallback):
    super(IdleHandler, self).__init__()

    self.daemon = True
    self.maxTicks = 3
    self.maxIdleTime = config.maxIdleTime
    self.previousIdleTime = 0
    self.isIdle = False
    self.currentTicks = 0
    self.idleCallback = idleCallback
    self.activeCallback = activeCallback
    self.debug = False
 
  def getIdleTime(self):
    raise NotImplementedError

  def setDebug(self, on):
    self.debug = on

  def run(self):
    print('%s Started.' % __class__.__name__)
    while True:
      newIdleTime = self.getIdleTime()
      delta = abs(self.previousIdleTime - newIdleTime)
      if newIdleTime > self.maxIdleTime and not self.isIdle:
        # user became idle, start jobs
        if self.debug:
          print('User became idle, starting jobs.')
        self.isIdle = True
        self.idleCallback()
      elif self.isIdle:
        if delta < 0.5:
          if self.currentTicks > self.maxTicks:
            # user became active, stop jobs
            if self.debug:
              print('User became active, stopping jobs.')
            self.currentTicks = 0
            self.isIdle = False
            self.activeCallback()
          else:
            # activity tick
            if self.debug:
              print('Activity tick.')
            self.currentTicks += 1
        else:
          self.currentTicks = 0
          self.isIdle = True
      else:
        # user remain active, do nothing
        self.currentTicks = 0
        self.isIdle = False

      self.previousIdleTime = newIdleTime
      sleep(1)

