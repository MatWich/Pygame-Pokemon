import pygame
from config import *


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        pygame.sprite.Sprite.__init__(self, self.game.all_sprites)
        # self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        # self.image.fill(RED)
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.rect.left = x * TILE_SIZE
        self.rect.top = y * TILE_SIZE

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        """ Sterowanie """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            print("csdc")
        elif keys[pygame.K_d]:
            self.rect.left += 5
        elif keys[pygame.K_a]:
            self.rect.left -= 5
        elif keys[pygame.K_w]:
            self.rect.top -= 5
        elif keys[pygame.K_s]:
            self.rect.top += 5


