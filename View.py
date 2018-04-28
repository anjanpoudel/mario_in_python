import pygame
import time

from pygame.locals import*
from time import sleep
from Model import Model

class View():

    print("This is view class ")

    #--------------------------
    #constructor for View
    #---------------------------
    def __init__(self, model):
        # print("This is view class, init")
        self.model = model
        screen_size = (800,600)
        self.screen = pygame.display.set_mode(screen_size, 32)
        self.bg_image = pygame.image.load("background.png")
        #Adding tube image
        self.tube_image = self.model.tube1.img

        self.fire_image = pygame.image.load("fireball_image.png")

        # Adding mario image
        self.marios = ["mario_1.png", "mario_2.png", "mario_3.png", "mario_4.png", "mario_5.png"]
        self.mario_images = []
        for m in self.marios:
            self.mario_images.append(pygame.image.load(m));

        #Adding gumba on screen
        self.gumba_img = pygame.image.load("gumba_image.png")
        self.gumba_fire_ing = pygame.image.load("gumba_fire_image.png")
        self.model.rect_gumba = self.gumba_img.get_rect()



    #--------------------------
    #Updates view
    #---------------------------
    def update(self):
        # print("This is view class, update")
        #rendering backgroung on screen
        self.screen.blit(self.bg_image, (0, 0))

        #rendering two tubes on screen
        self.screen.blit(self.tube_image,(self.model.tube1.x,self.model.tube1.y))
        self.screen.blit(self.tube_image,(self.model.tube2.x,self.model.tube2.y))

        #rendering all marios to test
        i = self.model.mario.get_mario_pos()
        # print("---- ", i )
        self.screen.blit(self.mario_images[i],(self.model.mario.x, self.model.mario.y))
        self.screen.blit(self.gumba_img,(self.model.gumba.x,self.model.gumba.y))
        self.draw_fire()

        pygame.display.flip()




    def draw_fire(self):
        print("Fire drawn")

        for m in self.model.fire_list:
            fire = m
            self.screen.blit(self.fire_image,(fire.x,fire.y))

        print("Is fire dwawn")
