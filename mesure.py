import pygame
from pygame.locals import *
from settings import *
from rythme import *
import random

def draw_text(screen, text, font, text_color, x, y):
	'''Fonction qui prend en entrée la surface ou on écrit le texte,
	la font du texte ainsi que sa couleur et sa position d'affichage'''
	img = font.render(text, True, text_color)
	#On convertie le texte en image
	screen.blit(img, (x,y))
	#On affiche l'image à la positon donnée


class Mesure:

    def __init__(self, pos_y = 100, index = 0, temps = 64, valeur="C", hauteur=4, dure=64):
        self.font = pygame.font.Font(None, 25)
        self.index = index
        self.temps = temps
        self.pos_y = pos_y
        self.pos_x = (index % 2) * ((WINDOW_WIDTH - 160) //2) + 160
        self.liste_rythme = list()
        self.display_surface = pygame.display.get_surface()
        self.generate_rythme()

    def generate_rythme(self):
        i = 0
        while i != self.temps:
            choix = random.choice([8,16,32,64])
            if choix + i <= self.temps :
                rythme = Rythme(dure = choix, pos_x= self.pos_x + (i * (((WINDOW_WIDTH - 160) //2)- 20)//64) + 20, pos_y = self.pos_y)
                self.liste_rythme.append(rythme)
                i += choix

    def move(self):
        self.pos_y -= 350
        for rythme in self.liste_rythme:
            rythme.move()
            
    def display(self):
        draw_text(self.display_surface, str(self.index), self.font, (255,255,255), self.pos_x - 10, self.pos_y - 30)
        pygame.draw.line(self.display_surface, BLANC, (self.pos_x, self.pos_y), (self.pos_x, self.pos_y + 160), 4)
        for rythme in self.liste_rythme:
            rythme.display()

