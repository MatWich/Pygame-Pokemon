import pygame
pygame.font.init()
from os import path

# SCREEN VARIABLES
SCR_SIZE = (WIDTH, HEIGHT) = (620, 480)
TITLE = "Pygame Pokemon"
FPS = 60

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# FONTS
dialogFont = pygame.font.SysFont('comicsans', 20)    #npcs dialogs

# LABELS
TILE_SIZE=32
GAME_FOLDER = path.dirname(__file__)
MAP_FOLDER = path.join(GAME_FOLDER, "maps")
IMG_FOLDER = path.join(GAME_FOLDER, "imgs")
PLAYER_IMG_FOLDER = path.join(IMG_FOLDER, "player")
ENEMY_IMG = "walker.png"

# DIALOUGES


# MAPS
LOCATION_1 = "location_1"

# IMAGES
PLAYER_IMG_PATH = "images/prof.png"
NPC1_IMG_PATH = "images/NPC1.png"
GRASS_IMG_PATH="images/Grass.png"
SAND_IMG_PATH="images/Sand.png"
SPRITE_NOT_FOUND_PATH="images/sprite_not_found.png"
TALL_GRASS_IMG_PATH="images/tall_grass.png"


def collide_hit_rect(sp1, sp2):
    return sp1.hit_rect.colliderect(sp2.rect)


def wall_colision_detection(sprite, group, dir):
    if dir == 'x':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery > 0:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y