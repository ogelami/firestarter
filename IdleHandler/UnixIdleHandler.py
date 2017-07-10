from IdleHandler import IdleHandler
from glob import glob
from datetime import datetime
from threading import Thread
import datetime

class UnixIdleHandler(IdleHandler):
	def __init__(self):
		super(UnixIdleHandler, self).__init__()
		keyboardDevices = glob('/dev/input/by-id/*-kbd')
		for keyboardDevice in keyboardDevices:
			thread = Thread(target = self.waitForInput, args=(self.tick), daemon = True)
			thread.start()
	
	def getIdleTime(self):
		return 0

	def tick(self):
		print(datetime.utcnow().timestamp())

	def waitForInput(self, callback)
		while True:
			with open(keyboardDevice, 'rb') as fileHandler:
				fileHandler.read(1)
				callback()