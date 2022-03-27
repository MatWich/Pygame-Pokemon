import pygame
from config import *
vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        pygame.sprite.Sprite.__init__(self, self.game.all_sprites)
        # self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))
        # self.image.fill(RED)
        self.pos = vec(x, y) * TILE_SIZE
        self.pos.x += TILE_SIZE / 2
        self.pos.y += TILE_SIZE / 2
        self.image = pygame.transform.scale(pygame.image.load("images/prof.png").convert_alpha(), (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.hit_rect = self.rect.copy()

        self.vel = vec(0, 0)


    def draw(self, screen, adjusted_rect):
        screen.blit(self.image, adjusted_rect)

    def update(self):
        """ Sterowanie """
        self.controls()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt

        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')
        self.rect.center = self.hit_rect.center  # niby dzila tez bez tego


    def controls(self):
        keys = pygame.key.get_pressed()
        self.vel = vec(0 ,0)
        if keys[pygame.K_SPACE]:
            print("csdc")
        elif keys[pygame.K_d]:
            self.vel.x = 100
        elif keys[pygame.K_a]:
            self.vel.x = -100
        elif keys[pygame.K_w]:
            self.vel.y = -100
        elif keys[pygame.K_s]:
            self.vel.y = 100


