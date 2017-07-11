from Quartz.CoreGraphics import *

class OsxIdleHandler(IdleHandler):
	def __init__(self, idleCallback, activeCallback):
		super(UnixIdleHandler, self).__init__(idleCallback, activeCallback)
		self.NX_ALLEVENTS = int(4294967295)

	def getIdleTime(self):
		idle = CGEventSourceSecondsSinceLastEventType(1, self.NX_ALLEVENTS)
		print(idle)
		return 0