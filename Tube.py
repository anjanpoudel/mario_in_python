import pygame
from pygame.locals import*

class Tube():
    #--------------------------
    #constructor for Tube
    #---------------------------
    def __init__(self, xx , yy):
        print("constructoi is dworkifn")
        self.x = xx
        self.y = yy
        self.width = 55
        self.hight = 400
        self.img = pygame.image.load("tube.png")
    #--------------------------
    #Updates tube
    #---------------------------
    def update(self):
        print("This is a update fir a updaye: ")


# tube1 = Tube(10,10)
