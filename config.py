import pygame
pygame.font.init()
from os import path

# SCREEN VARIABLES
WIDTH = 620
HEIGHT = 480
SCREEN_SIZE = (WIDTH, HEIGHT)

TITLE = "Pygame Pokemon"
FPS = 60

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# SCALE SPRITES
SCALE = 32

# TILE MAP STRUCTURES
mapTileImage = {
    "G": pygame.transform.scale(pygame.image.load("images/Grass.png"), (SCALE, SCALE)),
    "S": pygame.transform.scale(pygame.image.load("images/Sand.png"), (SCALE, SCALE)),
}

# FONTS
dialogFont = pygame.font.SysFont('comicsans', 20)    #npcs dialogs

# LABELS

TILE_SIZE=32
GAME_FOLDER = path.dirname(__file__)
MAP_FOLDER = path.join(GAME_FOLDER, "maps")
IMG_FOLDER = path.join(GAME_FOLDER, "imgs")
PLAYER_IMG_FOLDER = path.join(IMG_FOLDER, "player")
ENEMY_IMG = "walker.png"
SCR_SIZE = (WIDTH, HEIGHT) = (600, 500)
# DIALOUGES


# IMAGES
PLAYER_IMG_PATH = "images/prof.png"
NPC1_IMG_PATH = "images/Sand.png"
GRASS_IMG_PATH="images/Grass.png"

# Funkcje wspolne dla wszystkich spritow pewnie bd mozna je jakos we wzorcach powstawiac
def collide_hit_rect(sp1, sp2):
    return sp1.hit_rect.colliderect(sp2.rect)

def collide_with_walls(sprite, group, dir):
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