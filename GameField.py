import random
import pygame
import Screen
import Consts

game_field = []
mines_list = []


def create_game_field():
    global game_field
    for row in range(Consts.FIELD_ROWS):
        row = []
        for col in range(Consts.FIELD_COLS):
            row.append(Consts.EMPTY_SQUARE)
        game_field.append(row)


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
        Screen.pygame.transform(Consts.GRASS_IMG, (line, column))
        grass_list.append((line, column))
    return grass_list


def put_mines_in_grid():
    mines_num = random.randint(1, len(put_grass_in_grid()))
    for place in range(len(put_grass_in_grid())):
        for num in range(mines_num):
            mines_place = random.randint(1, len(put_grass_in_grid()))
            mines_list.append(put_grass_in_grid()[mines_place])
            pygame.surface.blit(Consts.MINE_IMG, Consts.GRASS_IMG, put_grass_in_grid()[mines_place])

        #
        #
        #
        #
        #
        # line = random.randint(0, 25)
        # column = random.randint(0, 50)
        # while line == 0 and column == 0 or line == 25 and column == 50:
        #     line = random.randint(0, 25)
        #     column = random.randint(0, 50)
        # mines_list.append((line, column))
        # screen.pygame.transform(mine_image, (line, column))


def soldier_slot1():
    for row in game_field:
        for column in row:
            for i in mines_list:
                if column != Consts.EMPTY_SQUARE and (column != i[1] and row != i[0]):
                    return (row, column)


def soldier_location():
    soldier_slots = []
    for row in range(soldier_slot1()[0], soldier_slot1()[1] + 4):
        for column in range(soldier_slot1()[1], soldier_slot1()[1] + 1):
            soldier_slots.append((row, column))
    return soldier_slots


def should_soldier_pop():
    if soldier_location()[-1] in mines_list and soldier_location()[-2] in mines_list:
        return True
    return False


def flag_location():


# screen.pygame.transform(flag_image, (21, 46))
# for row in range(21, 21 + 3):
#     for column in range(46, 46 + 4):


def touching_flag():
    if soldier_location()[-1]
# for row in mines_list:
#     if  soldier_location()[-1][0] == row
#
# return len(same_color_cluster) >= consts.MIN_CLUSTER_SIZE_TO_POP
