import pygame
import classes.game

from config import *
vec2 = pygame.math.Vector2


class BaseSprite(pygame.sprite.Sprite):
    def __init__(self, imagePath: str, game, groups: pygame.sprite.Group, x: int, y: int):
        if groups is None:
            self.groups = game.all_sprites
        else:
            self.groups = groups
        pygame.sprite.Sprite.__init__(self, self.groups)
        if imagePath is None or imagePath.__eq__(""):
            self.image = pygame.transform.scale(pygame.image.load(SPRITE_NOT_FOUND_PATH).convert_alpha(), (TILE_SIZE, TILE_SIZE))
        else:
            self.image = pygame.transform.scale(pygame.image.load(imagePath).convert_alpha(), (TILE_SIZE, TILE_SIZE))
        self.game = game
        self.pos = vec2(x, y) * TILE_SIZE
        self.pos.x += TILE_SIZE / 2
        self.pos.y += TILE_SIZE / 2
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def draw(self, screen, camera):
        screen.blit(self.image, camera.apply(self))

    def update(self):
        pass
