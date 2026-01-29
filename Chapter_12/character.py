import pygame

class Character():

    def __init__(self, bs_game):
        self.screen = bs_game.settings.screen
        self.screen_rect = bs_game.screen.get_rect()

        self.image = pygame.image.load("./images/character.bmp")
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)