import config
import pygame

class Npc:
    def __init__(self, x, y):
        self.position = [x, y]
        self.img = pygame.transform.scale(config.NPC1_IMG, (config.SCALE, config.SCALE))
        self.rect = pygame.Rect(self.position[0] * config.SCALE, self.position[1] * config.SCALE, config.SCALE, config.SCALE)

    def render(self, screen):
        self.rect = self.rect = pygame.Rect(self.position[0] * config.SCALE, self.position[1] * config.SCALE, config.SCALE, config.SCALE)
        screen.blit(self.img, self.rect)