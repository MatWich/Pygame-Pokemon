from classes.camera import Camera
from classes.game_state import GameState
from classes.map_container import MapContainer
from classes.object_factory import ObjectFactory
from classes.tile_factory import TileFactory
from config import *


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
        pygame.display.set_icon(pygame.image.load(PLAYER_IMG_PATH).convert_alpha())

    def change_map(self, name):
        fg_map_name = "objects_" + name
        bg_map_name = "tiles_" + name
        self.map_bg = self.mapContainer.getMap(bg_map_name)
        self.map = self.mapContainer.getMap(fg_map_name)
        if self.camera is None:
            pass
        else:
            self.camera.adjust(self.map_bg.width, self.map_bg.height)
            self.remove_sprites_from_groups()
            self.set_up()

    def remove_sprites_from_groups(self):
        self.all_sprites.empty()
        self.objects.empty()
        self.tiles.empty()
        self.npcs.empty()
        self.walls.empty()
        self.teleports.empty()
        self.grass.empty()

    def set_up(self):
        self.create_sprite_groups()

        for row, tiles in enumerate(self.map_bg.data):
            for col, tile in enumerate(tiles):
                TileFactory.get_sprite(self, tile, col, row)

        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                ObjectFactory.get_sprite(self, tile, col, row)

        if self.camera is None:
            self.camera = Camera(self.map_bg.width, self.map_bg.height)

    def create_sprite_groups(self):
        self.all_sprites = pygame.sprite.Group()
        self.objects = pygame.sprite.Group()
        self.tiles = pygame.sprite.Group()
        self.npcs = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.teleports = pygame.sprite.Group()
        self.grass = pygame.sprite.Group()

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

        for sprite in self.tiles:
            sprite.draw(self.screen, self.camera)

        for sprite in self.objects:
            sprite.draw(self.screen, self.camera)
        pygame.display.update()

    def draw_grid(self):
        for x in range(0, WIDTH, TILE_SIZE):
            pygame.draw.line(self.screen, (100, 100, 100), (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pygame.draw.line(self.screen, (100, 100, 100), (0, y), (WIDTH, y))

    def quit(self):
        self.run = False
        self.state = GameState.ENDED
        pygame.quit()
