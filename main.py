import pygame, sys
from pygame.locals import *
from settings import *
from porter import *

class Main():
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Partition")
        self.clock = pygame.time.Clock()

    def run(self):
        porter = Porter()
        while True:
            self.clock.tick(60)
            self.display_surface.fill(NOIR)
            for event in pygame.event.get():
				#Gestion des intéractions avec la fenêtre
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            porter.display()
            pygame.display.flip()


if __name__ == '__main__':
    main = Main()
    main.run()