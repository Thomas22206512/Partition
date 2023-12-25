import pygame
from pygame.locals import *
from settings import *
from mesure import * 

class Porter():

    def __init__(self, index=0, clef="sol", temps = 64, valeur="C", hauteur=4, dure=64):
        self.clef = clef
        self.index = index
        self.pos_y = index* 350 + 150
        self.display_surface = pygame.display.get_surface()
        self.liste_mesure = list()
        self.temps = temps
        self.generate_mesure()

    def generate_mesure(self):
        for i in range(2):
            mesure = Mesure(pos_y = self.pos_y, index= i + 2*self.index)
            self.liste_mesure.append(mesure)

    def move(self):
        self.pos_y -= 350
        for mesure in self.liste_mesure:
            mesure.move()

    def display(self):
        for i in range(5):
            pygame.draw.line(self.display_surface, BLANC, (0,self.pos_y + i * 40), (WINDOW_WIDTH, self.pos_y+ i*40), 4)
        for mesure in self.liste_mesure:
            mesure.display()

