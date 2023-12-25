import pygame, sys
from pygame.locals import *
from settings import *
from note import *
import random

def draw_text(screen, text, font, text_color, x, y):
	'''Fonction qui prend en entrée la surface ou on écrit le texte,
	la font du texte ainsi que sa couleur et sa position d'affichage'''
	img = font.render(text, True, text_color)
	#On convertie le texte en image
	screen.blit(img, (x,y))
	#On affiche l'image à la positon donnée

class Rythme:

    def __init__(self, dure, valeur="C", pos_x = 100, pos_y = 100, hauteur=4):
        self.font = pygame.font.Font(None, 25)
        self.dure = dure
        self.valeur = valeur
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hauteur = hauteur
        self.liste_note = list()
        self.display_surface = pygame.display.get_surface()
        self.generate_note()

    def generate_note(self):
        note = Note(valeur=random.choice(NOTES), pos_x=self.pos_x, pos_y = self.pos_y, hauteur=random.choice([4,5]), dure=self.dure)
        self.liste_note.append(note)

    def move(self):
        self.pos_y -= 350
        for note in self.liste_note:
            note.move()
            
    def display(self):
        # draw_text(self.display_surface, str(self.dure), self.font, BLANC, self.pos_x, self.pos_y)
        for note in self.liste_note:
            note.display()




