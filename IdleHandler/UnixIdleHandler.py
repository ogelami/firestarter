from IdleHandler import IdleHandler
from glob import glob
from threading import Thread
import datetime

class UnixIdleHandler(IdleHandler):
	def __init__(self, idleCallback, activeCallback):
		super(UnixIdleHandler, self).__init__(idleCallback, activeCallback)
		keyboardDevices = glob('/dev/input/by-id/*-kbd')
		self.lastKeyboardEvent = datetime.datetime.utcnow().timestamp()
		for keyboardDevice in keyboardDevices:
			thread = Thread(target = self.waitForInput, args = (keyboardDevice, self.tick), daemon = True)
			thread.start()
	
	def getIdleTime(self):
		return datetime.datetime.utcnow().timestamp() - self.lastKeyboardEvent

	def tick(self):
		self.lastKeyboardEvent = datetime.datetime.utcnow().timestamp()

	def waitForInput(self, keyboardDevice, callback):
		while True:
			with open(keyboardDevice, 'rb') as fileHandler:
				fileHandler.read(1)
				callback()
