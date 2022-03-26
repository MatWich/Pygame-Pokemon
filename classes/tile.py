import config
import pygame
from config import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, image=None):
        self.game = game
        pygame.sprite.Sprite.__init__(self, game.all_sprites)
        if image is None:
            self.image = pygame.image.load(NPC1_IMG_PATH).convert_alpha()
        else:
            self.image = image
        self.rect = self.image.get_rect()
        self.rect.left = x * TILE_SIZE
        self.rect.top = y * TILE_SIZE

    def draw(self, screen, rect):
        screen.blit(self.image, rect)

