import pygame

FLAG_NUM = 3
MINE_NUM = 2
GRASS_NUM = 1
EMPTY_SQUARE_NUM = 0
CONSTS_NUM = -1
RUNNING_STATE = 30
FIELD_ROWS = 25  # height
FIELD_COLS = 50  # width
WINDOW_HEIGHT = 10 * FIELD_ROWS
WINDOW_WIDTH = 10 * FIELD_COLS
MARGIN = 1
EMPTY_SQUARE = "EMPTY"

MINE_IMG = pygame.image.load('mine.png')

FLAG_IMG = pygame.image.load('flag.png')

GRASS_IMG = pygame.image.load('grass.png')
GRASS_WIDTH = 4
GRASS_HEIGHT = 3


SOLDIER_REG_IMG = "solider.png"
SOLDIER_NIGHT_IMG = "solider_nigth.png"
SOLDIER = pygame.image.load(SOLDIER_REG_IMG)

STARTING_POSITION = (0, 0)
