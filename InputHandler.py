from threading import Thread
import msvcrt

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