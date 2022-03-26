import pygame
from config import *


class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)  # bedzie sprawdzaxc jak daleko jest sie od konca mapy
        self.width = width
        self.height = height

    def apply(self, entity) -> pygame.Rect:
        return entity.rect.move(self.camera.topleft)

    def update(self, target):  # target == lapyer
        x = -target.rect.centerx + int(WIDTH / 2)
        y = -target.rect.centery + int(HEIGHT / 2)

        # nie moze pokazywac tego co jes za mapa
        x = min(0, x)  # left
        y = min(0, y)  # top
        x = max(- (self.width - WIDTH), x)  # right
        y = max(- (self.height - HEIGHT), y)  # bottom
        self.camera = pygame.Rect(x, y, self.width, self.height)