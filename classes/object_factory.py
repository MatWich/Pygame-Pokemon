from classes.player import Player
from classes.tall_grass import TallGrass
from classes.teleport import Teleport
from classes.wall import Wall
from config import *


class ObjectFactory:

    @staticmethod
    def get_sprite(game, key: str, x, y):
        if key is None or key.__eq__('.'):
            return
        if key.__eq__('P'):
            game.player = Player(PLAYER_IMG_PATH, game, (game.all_sprites, game.objects), x, y)
        elif key.__eq__('W'):
            Wall(NPC1_IMG_PATH, game, (game.all_sprites, game.objects, game.walls), x, y)
        elif key.__eq__('D'):
            Teleport(None, game, (game.all_sprites, game.objects, game.teleports), x, y)
        elif key.__eq__('T'):
            TallGrass(TALL_GRASS_IMG_PATH, game, (game.all_sprites, game.objects, game.grass), x, y)
        else:
            raise Exception("Wrong parameters passed to TileFactory.get_sprite() function")



