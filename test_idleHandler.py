#!/usr/bin/env python3

import platform

platformName = platform.system()

if platformName == 'Linux':
  from IdleHandler.UnixIdleHandler import UnixIdleHandler as IdleHandler
elif platformName == 'Windows':
  from IdleHandler.WindowsIdleHandler import WindowsIdleHandler as IdleHandler
elif platformName == 'Darwin':
	from IdleHandler.OsxIdleHandler import OsxIdleHandler as IdleHandler

from time import sleep

def x():
 print('a')

def y():
 print('b')

u = IdleHandler(x, y)
u.setDebug(True)
u.start()

while True:
 sleep(1)
