import pygame
import random
import Consts

pygame.init()
size = (Consts.FIELD_COLS, Consts.FIELD_ROWS)
screen = pygame.display.set_mode(size)
green_color = (124, 252, 0)
screen.fill(green_color)


def put_grass_in_grid():
    grass_list = []
    check = (0, 0)
    for num in range(20):
        line = random.randint(0, 25)
        column = random.randint(0, 50)
        while line == 0 and column == 0 or line == 25 and column == 50 or check in grass_list:
            line = random.randint(0, 25)
            column = random.randint(0, 50)
            check = (line, column)
        pygame.transform(Consts.GRASS_IMG, (line, column))
        grass_list.append((line, column))
    return grass_list
