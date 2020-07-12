import pygame
import config
import os

class Player:

    def __init__(self, x, y):
        self.position = [x, y]
        self.image = pygame.transform.scale(config.PLAYER_IMG, (config.SCALE, config.SCALE))  # LOADING IMAGE & SCALE IT
        self.rect = pygame.Rect(self.position[0] * config.SCALE, self.position[1] * config.SCALE, config.SCALE, config.SCALE)  # STORING RECTANGLE COORS OF PLAYER

    def updatePosition(self, newPos):
        self.position[0] += newPos[0]
        self.position[1] += newPos[1]

    def render(self, screen):
        pygame.draw.rect(screen, config.WHITE,
                         (self.position[0] * config.SCALE, self.position[1] * config.SCALE, config.SCALE, config.SCALE))

