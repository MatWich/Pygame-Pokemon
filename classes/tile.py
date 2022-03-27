import pygame
from config import *
vec = pygame.math.Vector2


class Tile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, image=None):
        self.game = game
        pygame.sprite.Sprite.__init__(self, game.all_sprites)
        if image is None:
            self.image = pygame.transform.scale(pygame.image.load(NPC1_IMG_PATH).convert_alpha(), (TILE_SIZE, TILE_SIZE))
        else:
            self.image = image
        self.rect = self.image.get_rect()
        self.pos = vec(x, y) * TILE_SIZE
        self.rect.center = self.pos
        # self.rect.y = y * TILE_SIZE

    def update(self):
        pass

    def draw(self, screen, rect):
        screen.blit(self.image, rect)

