import pygame
import random
from os import path
from config import *
from classes.map import Map
from classes.camera import Camera
from classes.player import Player
from classes.tile import Tile


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(SCR_SIZE)
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.counter = 0
        self.load_data()
        self.set_up()

    def load_data(self):
        self.map_bg = Map(path.join(MAP_FOLDER, "map2.txt"))
        self.map = Map(path.join(MAP_FOLDER, "map3.txt"))

        self.player_img = pygame.image.load(PLAYER_IMG_PATH).convert_alpha()
        self.player_img = pygame.transform.scale(self.player_img, (TILE_SIZE, TILE_SIZE))

        self.enemy_img = pygame.image.load(NPC1_IMG_PATH).convert_alpha()
        self.enemy_img = pygame.transform.scale(self.enemy_img, (TILE_SIZE, TILE_SIZE))

        self.grass_image = pygame.image.load(GRASS_IMG_PATH).convert_alpha()
        self.grass_image = pygame.transform.scale(self.grass_image, (TILE_SIZE, TILE_SIZE))

        pygame.display.set_icon(self.enemy_img)

    def set_up(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        for row, tiles in enumerate(self.map_bg.data):
            for col, tile in enumerate(tiles):
                self.what_to_create(tile, row, col)

        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                self.what_to_create(tile, row, col)

        self.camera = Camera(self.map.width, self.map.height)

    def mainloop(self):
        self.run = True
        while self.run:
            self.dt = self.clock.tick(FPS) / 1000
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
        self.all_sprites.draw(self.screen)
        for sprite in self.all_sprites:
            if isinstance(sprite, Tile):
                sprite.draw(self.screen, self.camera.apply(sprite))

        self.player.draw(self.screen)
        pygame.display.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(self.screen, (100, 100, 100), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.line(self.screen, (100, 100, 100), (0, y), (WIDTH, y))

    def what_to_create(self, tile, row, col):
        if tile == 'P':
            self.player = Player(self, col, row)

        elif tile == 'G':
            if self.counter % 2 == 0:
                Tile(self, col, row)
            else:
                Tile(self, col, row, self.grass_image)
            self.counter+=1


    def quit(self):
        self.run = False
        pygame.quit()