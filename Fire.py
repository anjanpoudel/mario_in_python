import pygame
from pygame.locals import*

class Fire():
    #--------------------------
    #constructor for Tube
    #---------------------------
    def __init__(self, xx , yy):
        self.x = xx
        self.y = yy
        self.vert_vel = -12
        self.img = pygame.image.load("fireball_image.png")
    #--------------------------
    #Updates tube
    #---------------------------
    def update(self):
        print("This is a update fir a updaye: ")
        self.x+=7;

        self.vert_vel += 2.2
        self.y += self.vert_vel

        if self.y > 355:
            # self.vert_vel = 2.2
            self.y = self.y - 50



fire1 = Fire(10,10)
