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
        player = Player(1, 1)
        self.player = player        # For keyEvents to be able to move player
        self.objects.append(player)
        self.gameState = GameStat.RUNNING


    def update(self):
        self.screen.fill(config.BLACK)
        self.keyEvents()

        # ADDING obj to the screen like player npcs
        for obj in self.objects:
            obj.render(self.screen)

        pygame.display.update() # REFRESHES WINDOW


    def keyEvents(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.gameState = GameStat.ENDED
            # Keydown events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.gameState = GameStat.ENDED
                # MOVEMENT
                elif event.key == pygame.K_w:
                    self.player.updatePosition([0, -1])
                elif event.key == pygame.K_s:
                    self.player.updatePosition([0, 1])
                elif event.key == pygame.K_a:
                    self.player.updatePosition([-1, 0])
                elif event.key == pygame.K_d:
                    self.player.updatePosition([1, 0])

