import pygame
from pygame.locals import *
from settings import *

class Lecteur:
    def __init__(self, speed = 10, pos_x = 160, pos_y = 150):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed
        self.display_surface = pygame.display.get_surface()

    def display(self):
        box = pygame.Rect(self.pos_x, self.pos_y, 10, 160)
        pygame.draw.rect(self.display_surface, (0,255,255), box, width=0)

    def move(self):
        self.pos_x += self.speed

