import pygame

from classes.base_sprite import BaseSprite
from config import *


class Teleport(BaseSprite):
    def __init__(self, imagePath: str, game, groups, x: int, y: int):
        super().__init__(imagePath, game, groups, x, y)

    def draw(self, screen, camera):
        super().draw(screen, camera)

    def update(self):
        super().update()
        if self.detect_collision_with_player(self.game.player):
            print("TODO: Teleport to other map")

    def detect_collision_with_player(self, player):
        return collide_hit_rect(player, self)

