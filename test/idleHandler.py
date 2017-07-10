#!/usr/bin/env python3

from IdleHandler.UnixIdleHandler import UnixIdleHandler
from time import sleep

def x():
 print('a')

def y():
 print('b')

u = UnixIdleHandler(x, y)
u.setDebug(True)
u.start()

while True:
 sleep(1)

