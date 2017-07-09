from threading import Thread
from ctypes import Structure, c_uint, sizeof, windll, byref
import config

#debugging only
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

  class LASTINPUTINFO(Structure):
    _fields_ = [
      ('cbSize', c_uint),
      ('dwTime', c_uint),
    ]
 
  def getIdleTime(self):
    lastInputInfo = self.LASTINPUTINFO()
    lastInputInfo.cbSize = sizeof(lastInputInfo)
    windll.user32.GetLastInputInfo(byref(lastInputInfo))

    return (windll.kernel32.GetTickCount() - lastInputInfo.dwTime) / 1000.0

  def run(self):
    print('%s Started.' % __class__.__name__)
    while True:
      newIdleTime = self.getIdleTime()
      delta = abs(self.previousIdleTime - newIdleTime)
      if newIdleTime > self.maxIdleTime and not self.isIdle:
        self.isIdle = True
        self.idleCallback()
#        print("Starting job")
      elif self.isIdle:
        if delta < 0.5:
          if self.currentTicks > self.maxTicks:
            self.currentTicks = 0
            self.isIdle = False
            self.activeCallback()
#            print('Stopping job')
          else:
#            print('Activity tick')
            self.currentTicks += 1
        else:
          self.currentTicks = 0
          self.isIdle = True
      else:
#        print('User is active')
        self.currentTicks = 0
        self.isIdle = False

      self.previousIdleTime = newIdleTime
      sleep(1)

