import pygame
from pygame.locals import *
from settings import *

class Note():
    def __init__(self, note="do", pos_x = 100, hauteur=4):
        self.note = note
        self.pos_x = pos_x
        self.hauteur = hauteur
        self.display_surface = pygame.display.get_surface()

    def move(self):
        self.pos_x -= 2
    
    def display(self):
        if self.hauteur == 4 :
            if self.note == "do":
                pygame.draw.line(self.display_surface, BLANC, (self.pos_x - 25,NOTE_DIC[self.note] + WINDOW_HEIGHT//2), (self.pos_x + 25, NOTE_DIC[self.note] + WINDOW_HEIGHT//2), 4)
            pygame.draw.circle(self.display_surface, BLANC, (self.pos_x, NOTE_DIC[self.note] + WINDOW_HEIGHT//2), 20, width=5)
        elif self.hauteur == 5 :
            if self.note == "la":
                pygame.draw.line(self.display_surface, BLANC, (self.pos_x - 25, NOTE_DIC[self.note] - 140 + WINDOW_HEIGHT//2), (self.pos_x + 25,  NOTE_DIC[self.note] - 140 + WINDOW_HEIGHT//2), 4)
            if self.note == "si":
                pygame.draw.line(self.display_surface, BLANC, (self.pos_x - 25, NOTE_DIC[self.note] - 160 + WINDOW_HEIGHT//2), (self.pos_x + 25,  NOTE_DIC[self.note] - 160 + WINDOW_HEIGHT//2), 4)
            pygame.draw.circle(self.display_surface, BLANC, (self.pos_x, NOTE_DIC[self.note] - 140 + WINDOW_HEIGHT//2), 20, width=5) 