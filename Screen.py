import pygame
import random
import Consts
import GameField

pygame.init()
size = (Consts.FIELD_COLS, Consts.FIELD_ROWS)
screen = pygame.display.set_mode(size)


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


font = pygame.font.SysFont('timesnewroman', 60)


def win_msg():
    win_txt = font.render("YOU WON!", False, (255, 255, 255))
    screen.blit(win_txt, (12.5, 225))
    pygame.display.update()


def lose_msg():
    win_txt = font.render("YOU LOST!", False, (255, 255, 255))
    screen.blit(win_txt, (12.5, 225))
    pygame.display.update()


def draw_game():
    screen.fill(Consts.green_color)
    GameField.create_game_field()
    if GameField.should_soldier_pop():
        lose_msg()
    elif GameField.touching_flag():
        win_msg()

    pygame.display.flip()
