from ctypes import Structure, c_uint, sizeof, windll, byref
from IdleHandler import IdleHandler

class WindowsIdleHandler(object):
	def __init__(self):
		super(WindowsIdleHandler, self).__init__()

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