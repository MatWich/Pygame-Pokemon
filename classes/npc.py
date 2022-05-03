import classes.base_sprite
from config import *


class NPC(classes.base_sprite.BaseSprite):
    def __init__(self, imagePath, game, groups, x, y):
        super(NPC, self).__init__(imagePath, game, groups, x, y)


