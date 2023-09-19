import pygame
import random
import Consts
import GameField



# img = pygame.transform.scale(Consts.SOLDIER_REG_IMG, (2 , 4 ))
# screen.blit(img,[0,0])

# screen.blit(Consts.green_color, (0,0))
# pygame.display.flip()
def make_screen():
    pygame.init()
    size = (Consts.WINDOW_WIDTH, Consts.WINDOW_HEIGHT)
    screen = pygame.display.set_mode(size)
    screen.fill(Consts.green_color)
    return screen
screen = make_screen()
pygame.display.flip()


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
# screen.blit(text_img, location)