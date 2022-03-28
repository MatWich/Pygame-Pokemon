from config import *
from classes.base_sprite import BaseSprite


class Wall(BaseSprite):
    def __init__(self, imagePath, game, groups, x, y):
        BaseSprite.__init__(self, imagePath, game, groups, x, y)

    def draw(self, screen, camera):
        super().draw(screen, camera)

    def update(self):
        super().update()


