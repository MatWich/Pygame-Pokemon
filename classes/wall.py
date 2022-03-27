import pygame
from config import *
vec = pygame.math.Vector2


class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        pygame.sprite.Sprite.__init__(self, game.walls)
        self.image = pygame.transform.scale(pygame.image.load(SAND_IMG_PATH).convert_alpha(), (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()
        self.pos = vec(x, y) * TILE_SIZE
        self.rect.center = self.pos

    def update(self):
        pass
