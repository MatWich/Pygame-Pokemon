import pygame
import config

class Player:
    def __int__(self, x, y):
        self.position = [x, y]
        self.image = pygame.transform.scale(pygame.image.load("/images/player/prof.png"), (config.SCALE, config.SCALE)) # LOADING IMAGE & SCALE IT
        self.rect = pygame.Rect(self.position[0] * config.SCALE, self.position[1] * config.SCALE, config.SCALE, config.SCALE)

    def update(self):
        pass

    def render(self, screen):
        pass
