import random

from classes.game_state import GameState
from config import *
from classes.base_sprite import BaseSprite


class TallGrass(BaseSprite):
    def __init__(self, imagePath, game, group, x, y):
        BaseSprite.__init__(self, imagePath, game, group, x, y)
        self.pokemonSpawned = False

    def draw(self, screen, camera):
        super().draw(screen, camera)

    def update(self):
        if self.detect_collision_with_player(self.game.player):
            self.spawn_a_pokemon()
        else:
            self.pokemonSpawned = False

    def detect_collision_with_player(self, player):
        return collide_hit_rect(player, self)

    def spawn_a_pokemon(self):
        if not self.pokemonSpawned:
            seed = random.randrange(0, 10)
            if seed < .01:
                print("Pokemon encountered")
                self.pokemonSpawned = True
                self.game.state = GameState.BATTLE

