import pygame
import sys
import config
from classes.game import Game, GameStat
pygame.init()

# SCREEN
screen = pygame.display.set_mode(config.SCREEN_SIZE)
pygame.display.set_caption(config.TITLE)

# GETTING STARTED
game = Game(screen)
game.setUp()

clock = pygame.time.Clock()

while game.gameState == GameStat.RUNNING:
    clock.tick(config.FPS)
    game.update()
