import pygame
pygame.font.init()

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

# IMAGES
PLAYER_IMG = pygame.image.load("images/player/prof.png")
NPC1_IMG = pygame.image.load("images/player/NPC1.png")
