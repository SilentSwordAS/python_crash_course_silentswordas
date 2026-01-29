import pygame

import sys

from settings import Settings
from character import Character

class BlueSky():

    def __init__(self):
        pygame.init()

        self.settings = Settings()
        self.screen = self.settings.screen

        pygame.display.set_caption("Alien Invasion")

        self.character = Character(self)
    
    def run_game(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.settings.bg_color)
            self.character.blitme()

            pygame.display.flip()

if __name__ == "__main__":
    bs = BlueSky()
    bs.run_game()