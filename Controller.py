import pygame
import time

from Model import Model
from pygame.locals import*
from time import sleep

class Controller():

    #--------------------------
    #constructor for Controller
    #---------------------------
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.keep_going = True
    #--------------------------
    #updates controller
    #---------------------------
    def update(self):
        self.model.mario.remember_state()
        for event in pygame.event.get():
            if event.type == QUIT:
                self.keep_going = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.keep_going = False
            elif event.type == pygame.MOUSEBUTTONUP:
                self.model.set_dest(pygame.mouse.get_pos())
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            self.model.mario.move_back()
        if keys[K_RIGHT]:
            self.model.mario.move_front()
        if keys[K_SPACE]:
            self.model.mario.mario_jump()
        if keys[K_LCTRL]:
            self.model.mario_fire()
            # self.view.draw_fire()
        if keys[K_RCTRL]:
            self.model.mario_fire()
            # self.view.draw_fire()
