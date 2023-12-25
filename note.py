import pygame
from pygame.locals import *
from settings import *

class Note():
    def __init__(self, valeur="C", pos_x = 100, pos_y = 100, hauteur=4, dure=64):
        self.valeur = valeur
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hauteur = hauteur
        self.dure = dure
        self.display_surface = pygame.display.get_surface()


    def move(self):
        self.pos_y -= 350
    
    def display(self):
        if self.hauteur == 4 :
            if self.valeur == "C":
                pygame.draw.line(self.display_surface, BLANC, (self.pos_x - 25,self.pos_y + NOTE_DIC[self.valeur]), (self.pos_x + 25, NOTE_DIC[self.valeur] + self.pos_y), 4)
            pygame.draw.circle(self.display_surface, BLANC, (self.pos_x, self.pos_y + NOTE_DIC[self.valeur]), 15, width=5 if self.dure >= 32 else 0)
        elif self.hauteur == 5 :
            if self.valeur == "A":
                pygame.draw.line(self.display_surface, BLANC, (self.pos_x - 25, NOTE_DIC[self.valeur] - 140 + self.pos_y), (self.pos_x + 25,  NOTE_DIC[self.valeur] - 140 + self.pos_y), 4)
            if self.valeur == "B":
                pygame.draw.line(self.display_surface, BLANC, (self.pos_x - 25, NOTE_DIC[self.valeur] - 120 + self.pos_y), (self.pos_x + 25,  NOTE_DIC[self.valeur] - 120 + self.pos_y), 4)
            pygame.draw.circle(self.display_surface, BLANC, (self.pos_x, NOTE_DIC[self.valeur] - 140 + self.pos_y), 15, width= 5 if self.dure >= 32 else 0)

        if self.dure <= 32:
            pygame.draw.line(self.display_surface, BLANC, (self.pos_x + 10, self.pos_y + NOTE_DIC[self.valeur] - (140 if self.hauteur == 5 else 0)), (self.pos_x + 10, self.pos_y + NOTE_DIC[self.valeur] + 10 - (140 if self.hauteur == 5 else 0) - 80), 4)

        if self.dure <= 8 :
            pygame.draw.line(self.display_surface, BLANC, (self.pos_x + 10, self.pos_y + NOTE_DIC[self.valeur] + 10 - (140 if self.hauteur == 5 else 0) - 80), (self.pos_x + 30 , self.pos_y + NOTE_DIC[self.valeur] + 10 - (140 if self.hauteur == 5 else 0) - 80), 4)

        if self.dure <= 4 : 
            pygame.draw.line(self.display_surface, BLANC, (self.pos_x + 10, self.pos_y + NOTE_DIC[self.valeur] + 20 - (140 if self.hauteur == 5 else 0) - 80), (self.pos_x + 30 , self.pos_y + NOTE_DIC[self.valeur] + 20 - (140 if self.hauteur == 5 else 0) - 80), 4)

        if self.dure <= 2 : 
            pygame.draw.line(self.display_surface, BLANC, (self.pos_x + 10, self.pos_y + NOTE_DIC[self.valeur] + 30 - (140 if self.hauteur == 5 else 0) - 80), (self.pos_x + 30 , self.pos_y + NOTE_DIC[self.valeur] + 30 - (140 if self.hauteur == 5 else 0) - 80), 4)

        if self.dure <= 1 : 
            pygame.draw.line(self.display_surface, BLANC, (self.pos_x + 10, self.pos_y + NOTE_DIC[self.valeur] + 40 - (140 if self.hauteur == 5 else 0) - 80), (self.pos_x + 30 , self.pos_y + NOTE_DIC[self.valeur] + 40 - (140 if self.hauteur == 5 else 0) - 80), 4)
