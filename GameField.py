import random
import pygame
game_field = []
FIELD_ROWS = 25
FIELD_COLS = 50
EMPTY_SQUARE = "EMPTY"
mines_list = []
mine_image = pygame.image.load('mine.png')


def create_game_field():
    global game_field
    for row in range(FIELD_ROWS):
        row = []
        for col in range(FIELD_COLS):
            row.append(EMPTY_SQUARE)
        game_field.append(row)

def put_mines_in_grid():
    mines_num = random.randint(1, 10)
    for num in range(mines_num):
        line = random.randint(0, 25)
        column = random.randint(0, 50)
        while line == 0 and column == 0 or line == 25 and column == 50:
            line = random.randint(0, 25)
            column = random.randint(0, 50)
        mines_list.append((line, column))
        a = (line, column)
        screen.blit(mine_image, (line, column))


def soldier_slot1():
    for row in game_field:
        for column in row:
            for i in mines_list:
                if column != EMPTY_SQUARE and (column != i[1] and row != i[0]):
                    return (row, column)
def soldier_location():
    soldier_slots = []
    for row in range(soldier_slot1()[0], soldier_slot1()[1] + 3):
        for column in range(soldier_slot1()[1], soldier_slot1()[1] + 1):
            soldier_slots.append((row, column))
    return soldier_slots

def should_soldier_pop():
    for row in mines_list:
    if soldier_location()[-1] ==

    return len(same_color_cluster) >= consts.MIN_CLUSTER_SIZE_TO_POP

