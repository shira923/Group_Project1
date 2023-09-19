import pygame
import random
import Consts
import GameField


pygame.init()
size = (Consts.FIELD_COLS, Consts.FIELD_ROWS)
screen = pygame.display.set_mode(size)




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
