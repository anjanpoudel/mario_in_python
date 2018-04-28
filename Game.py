import pygame
import time

from Model import Model
from View import View
from Controller import Controller
from pygame.locals import*
from time import sleep

print("Use the arrow keys to move. Press Esc to quit.\n")
m = Model()
v = View(m)
c = Controller(m,v)
while c.keep_going:
	c.update()
	m.update()
	v.update()
	sleep(0.04)
print("Goodbye")
