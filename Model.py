import pygame
import time

from Fire import Fire
from Tube import Tube
from Gumba import Gumba
from Mario import Mario
from pygame.locals import*
from time import sleep

class Model():
    #--------------------------
    #constructor for Model
    #---------------------------
    def __init__(self):
        self.gumba = Gumba()
        self.mario = Mario()
        # self.fire = Fire()
        self.tube1 = Tube(250,350)
        self.tube2 = Tube(600,250)

        self.tube_list = [self.tube1, self.tube2]
        print(self.tube_list[0])

        self.fire_list = []


    def does_collide(self,x1,y1,w1,h1,x2,y2,w2,h2):
        if x1 + w1 < x2:
            return False
        if x1 > x2 + w2:
            return False
        if y1 + h1 < y2:
            return False
        if y1 > y2 + h2:
            return False
        return True

    #--------------------------
    #constructor for update
    #---------------------------
    def update(self):
        # print("This is Model class, update");
        self.gumba.update()
        self.mario.update()

        for f in self.fire_list:
            self.fire_up = f
            print("This works hehe hehehehehheeh")
            self.fire_up.update()

        for i in range(0, 2) :
            self.tube = self.tube_list[i]
            if self.does_collide(self.mario.x, self.mario.y, self.mario.width, self.mario.hight, self.tube.x, self.tube.y, self.tube.width, self.tube.hight ):
                self.mario.get_out_of_tube(self.tube)

            if self.does_collide(self.gumba.x, self.gumba.y, self.gumba.width, self.gumba.hight, self.tube.x, self.tube.y, self.tube.width, self.tube.hight ):
                self.mario.get_out_of_tube(self.tube)
                self.gumba.collide = True;


    def mario_fire(self):
        print("Fire is made now draw")
        self.fire_list.append(Fire(self.mario.x, self.mario.y))


#
# model1 = Model()
# model1.mario_fire()
