from classes.tile import Tile
from config import *


class TileFactory:

    @staticmethod
    def get_sprite(game, key: str, x, y):
        if key.__eq__('S'):
            Tile(GRASS_IMG_PATH, game, (game.all_sprites, game.tiles), x, y)
        elif key.__eq__('G'):
            Tile(SAND_IMG_PATH, game, (game.all_sprites, game.tiles), x, y)
        else:
            raise Exception("Wrong parameters passed to TileFactory.get_sprite() function")
