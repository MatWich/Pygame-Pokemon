import pygame
import random
from os import path

from classes.game_state import GameState
from classes.map_container import MapContainer
from classes.tall_grass import TallGrass
from classes.teleport import Teleport
from config import *
from classes.camera import Camera
from classes.player import Player
from classes.tile import Tile
from classes.wall import Wall


class Game:
    def __init__(self, screen):
        pygame.init()
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.state = GameState.OPEN_WORLD
        self.player = None
        self.map = None
        self.map_bg = None
        self.mapContainer = MapContainer().loadMapPaths()
        self.camera = None
        self.counter = 0
        self.load_data()
        self.set_up()

    def load_data(self):
        self.change_map(LOCATION_1)

        self.player_img = pygame.image.load(PLAYER_IMG_PATH).convert_alpha()
        self.player_img = pygame.transform.scale(self.player_img, (TILE_SIZE, TILE_SIZE))

        self.enemy_img = pygame.image.load(NPC1_IMG_PATH).convert_alpha()
        self.enemy_img = pygame.transform.scale(self.enemy_img, (TILE_SIZE, TILE_SIZE))

        self.grass_image = pygame.image.load(GRASS_IMG_PATH).convert_alpha()
        self.grass_image = pygame.transform.scale(self.grass_image, (TILE_SIZE, TILE_SIZE))

        pygame.display.set_icon(self.enemy_img)

    def change_map(self, name):
        fg_map_name = "objects_" + name
        bg_map_name = "tiles_" + name
        self.map_bg = self.mapContainer.getMap(bg_map_name)
        self.map = self.mapContainer.getMap(fg_map_name)
        if self.camera is None:
            pass
        else:
            self.camera.adjust(self.map_bg.width, self.map_bg.height)
            self.all_sprites.empty()
            self.enemies.empty()
            self.teleports.empty()
            self.walls.empty()
            self.tiles.empty()
            self.grass.empty()
            self.set_up()
        # self.map_bg = self.mapContainer.getMap("objects_location_1")
        # self.map = self.mapContainer.getMap("tiles_location_1")

    def set_up(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.teleports = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()
        self.grass = pygame.sprite.Group()

        for row, tiles in enumerate(self.map_bg.data):
            for col, tile in enumerate(tiles):
                self.what_to_create(tile, row, col)

        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                self.what_to_create(tile, row, col)

        if self.camera is None:
            self.camera = Camera(self.map_bg.width, self.map_bg.height)

    def mainloop(self):
        self.events()
        self.update()
        self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw(self):
        pygame.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill((9, 0, 0))
        self.draw_grid()
        # self.all_sprites.draw(self.screen)

        for sprite in self.tiles:
            # self.screen.blit(sprite.image, self.camera.apply(sprite))
            sprite.draw(self.screen, self.camera)

        for sprite in self.grass:
            sprite.draw(self.screen, self.camera)
            # self.screen.blit(sprite.image, self.camera.apply(sprite))

        for sprite in self.teleports:
            sprite.draw(self.screen, self.camera)

        for sprite in self.walls:
            sprite.draw(self.screen, self.camera)
            # self.screen.blit(sprite.image, self.camera.apply(sprite))
        self.player.draw(self.screen, self.camera)
        pygame.display.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(self.screen, (100, 100, 100), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.line(self.screen, (100, 100, 100), (0, y), (WIDTH, y))

    def what_to_create(self, tile, row, col):
        if tile == 'P':
            self.player = Player(PLAYER_IMG_PATH, self, (self.all_sprites), col, row)

        elif tile == 'G':
            if self.counter % 2 == 0:
                Tile(SAND_IMG_PATH, self, (self.tiles, self.all_sprites), col, row)
            else:
                Tile(GRASS_IMG_PATH, self, (self.tiles, self.all_sprites), col, row)
            self.counter += 1

        elif tile == 'W':
            Wall(NPC1_IMG_PATH, self, (self.walls, self.all_sprites), col, row)

        elif tile == 'T':
            TallGrass(TALL_GRASS_IMG_PATH, self, (self.grass, self.all_sprites), col, row)

        elif tile == 'D':
            Teleport(None, self, (self.all_sprites, self.teleports), col, row)

        elif tile == 'S':
            Tile(SAND_IMG_PATH, self, (self.tiles, self.all_sprites), col, row)

    def quit(self):
        self.run = False
        self.state = GameState.ENDED
        pygame.quit()