from ctypes import Structure, c_uint, sizeof, windll, byref
from IdleHandler import IdleHandler

class WindowsIdleHandler(IdleHandler):
	def __init__(self, idleCallback, activeCallback):
		super(WindowsIdleHandler, self).__init__(idleCallback, activeCallback)

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