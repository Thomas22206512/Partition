import pygame, sys
from pygame.locals import *
from settings import *
from porter import *
from lecteur import *
import json

class Main():
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Partition")
        self.clock = pygame.time.Clock()
        self.liste_porter = list()
    
    # def lecture_partition(self):
    #     with open("partition.json", 'r', encoding='utf-8') as file :
    #         dic = json.load(file)
    #         file.close()
    #     for items,value in dic.items():
    #         pass

    def generate_porter(self, nombre):
        for i in range(nombre):
            porter = Porter(index = i)
            self.liste_porter.append(porter)

    def run(self):
        self.generate_porter(2000)
        lecteur = Lecteur(speed = 15)
        while True:
            self.clock.tick(30)
            self.display_surface.fill(NOIR)
            if self.liste_porter[-1].pos_y > 10:     
                lecteur.display()
                lecteur.move()
                if lecteur.pos_x >= WINDOW_WIDTH:
                    lecteur.pos_x = 160
                    for porter in self.liste_porter:
                        porter.move()
            for event in pygame.event.get():
				#Gestion des intéractions avec la fenêtre
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            for porter in self.liste_porter:
                if porter.pos_y >= 100 and porter.pos_y <= WINDOW_HEIGHT:
                    porter.display()
            pygame.display.flip()


if __name__ == '__main__':
    main = Main()
    main.run()