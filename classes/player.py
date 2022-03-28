from config import *
from classes.base_sprite import BaseSprite
vec = pygame.math.Vector2


class Player(BaseSprite):
    def __init__(self, imagePath, game, groups, x, y):
        BaseSprite.__init__(self, imagePath, game, groups, x, y)
        self.hit_rect = self.rect.copy()
        self.vel = vec(0, 0)

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


