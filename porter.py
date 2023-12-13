import pygame
from pygame.locals import *
from settings import *
from note import *

class Porter():

    def __init__(self,clef="sol"):
        self.clef = clef
        self.display_surface = pygame.display.get_surface()
        self.liste_note = list()
        self.random_note(8)


    def random_note(self,k):
        for i in range(k):
            note = Note(random.choice(NOTES),i*200 + 100, random.choice([4,5]))
            self.liste_note.append(note)

    def display(self):
        for i in [-80,-40,0,40,80]:
            pygame.draw.line(self.display_surface, BLANC, (0,WINDOW_HEIGHT//2 + i), (WINDOW_WIDTH, WINDOW_HEIGHT//2 + i), 4)
        for note in self.liste_note:
            if note.pos_x < -100 :
                note1 = Note(random.choice(NOTES), self.liste_note[-1].pos_x + 200, random.choice([4,5]))
                self.liste_note.append(note1)
                del self.liste_note[0]
            note.display()
            note.move()