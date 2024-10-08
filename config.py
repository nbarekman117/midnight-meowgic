import pygame
from constants import *


# Helper function to load and resize images
def load_and_resize_image(path, width, height):
    img = pygame.image.load(path)
    return pygame.transform.scale(img, (width, height))


# Load Player sprite sheet and extract frames
PLAYER_SPRITE_SHEET = pygame.image.load(PLAYER_IMAGE_PATH)
PLAYER_FRAMES = [
    PLAYER_SPRITE_SHEET.subsurface(pygame.Rect(i * PLAYER_FRAME_WIDTH, 0, PLAYER_FRAME_WIDTH, PLAYER_FRAME_HEIGHT))
    for i in range(3)  # 3 frames across
]
# Load MagicBall sprite sheet and extract frames
MAGICBALL_SPRITE_SHEET = pygame.image.load(MAGICBALL_SPRITE_PATH)
MAGICBALL_FRAMES = [
    MAGICBALL_SPRITE_SHEET.subsurface(pygame.Rect(col * LASER_WIDTH, row * LASER_HEIGHT, LASER_WIDTH, LASER_HEIGHT))
    for row in range(2) for col in range(4)
]

# Load Backgrounds
BACKGROUND1_IMG = load_and_resize_image(BACKGROUND1_PATH, WIDTH, HEIGHT)
BACKGROUND2_IMG = load_and_resize_image(BACKGROUND2_PATH, WIDTH, HEIGHT)
BACKGROUND3_IMG = load_and_resize_image(BACKGROUND3_PATH, WIDTH, HEIGHT)

# Load Enemy Bat sprite sheet and Explosion sprite sheet
BAT_SPRITE_SHEET = pygame.image.load(BAT_SPRITE_PATH)
EXPLOSION_SPRITE_SHEET = pygame.image.load(EXPLOSION_SPRITE_PATH)

# Load Ghost and Monster sprite sheets
GHOST_SPRITE_SHEET = load_and_resize_image(GHOST_SPRITE_PATH, 256, GHOST_FRAME_HEIGHT)
MONSTER_SPRITE_SHEET = load_and_resize_image(MONSTER_SPRITE_PATH, 1000, 250)
