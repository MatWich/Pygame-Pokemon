import pygame
import config
from classes.player import Player
from enum import Enum

class GameStat(Enum):
    NONE = 0
    RUNNING = 1
    ENDED = 2

class Game():
    def __init__(self, screen):
        self.screen = screen    # SCREEN FROM main.py
        self.gameState = GameStat.NONE  # For mainLoop
        self.objects = []   # FOR PLAYER NPCs etc
        self.map = []   # FOR TILE MAP FROM maps directory
        self.cameraX = 0    # it is for properly working camera in width
        self.camera = [0, 0]    # coords

    def setUp(self):
        player = Player()
        self.objects.append(player)
        self.gameState = GameStat.RUNNING


    def update(self):
        self.screen.fill(config.BLACK)
        self.keyEvents()

        for obj in self.objects:
            obj.render(self.screen)
        pygame.display.update()


    def keyEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameState = GameStat.ENDED
            # Keydown events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.gameState = GameStat.ENDED

