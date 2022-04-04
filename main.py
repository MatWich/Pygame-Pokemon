import pygame
from classes.game import Game
from classes.game_state import GameState
from config import *

screen = pygame.display.set_mode(SCR_SIZE)

game = Game(screen)
game.dt = game.clock.tick(FPS) / 1000

if __name__ == "__main__":
    while game.state != GameState.ENDED:
        game.clock.tick(FPS)

        if game.state == GameState.OPEN_WORLD:
            game.mainloop()

        if game.state == GameState.MENU:
            print("MENU TO DO")

        if game.state == GameState.BATTLE:
            print("BATTLE TO DO")