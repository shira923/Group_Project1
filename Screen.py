import pygame

FIELD_ROWS = 25
FIELD_COLS = 50

pygame.init()
size = (FIELD_COLS, FIELD_ROWS)
screen = pygame.display.set_mode(size)
green_color = (124, 252, 0)
screen.fill(green_color)

GRASS_IMG = "grass.png"
GRASS_WIDTH = 4
GRASS_HEIGHT = 3


def random_grass():
    grass = pygame.image.load(GRASS_IMG)
    sized_grass = pygame.transform.scale(grass, (GRASS_WIDTH, GRASS_HEIGHT))
    for i in range(20):

