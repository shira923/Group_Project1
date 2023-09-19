import random
import pygame
import Screen
import Consts

game_field = []
mines_list = []


def create(line, column):
    return {"number": None,
            "center_x": column * 10,
            "center_y": line * 10}


# def recalc_bubbles_locations():
#     # There is no need to do so for the first line, since it was just added
#     for row in range(1, len(game_field)):
#         for col in range(50):
#             game_field[row][col]["center_x"] = Bubble.calc_center_x(col, row,
#                                                                       row_start=0)
#             game_field[row][col]["center_y"] = Bubble.calc_center_y(row)


def create_game_field():
    global game_field
    for row in range(Consts.FIELD_ROWS):
        row = []
        for col in range(Consts.FIELD_COLS):
            row.append(Consts.EMPTY_SQUARE)
        game_field.append(row)


# def calc_center(col, row):
#     x = row * 10
#     y = col * 10
#     return (x , y)

# def calc_x():
#     x = col * 10

# def calc_center_x(col, row,):
#     x = row * 10
#     y = col * 10
#          col * (
#             Consts.BUBBLE_RADIUS * 2 + consts.SPACE_BETWEEN_COLS) + consts.BUBBLE_RADIUS
#
#     # Uneven rows has an offset
#     if row % 2 != 0:
#         bubble_x += consts.BUBBLE_RADIUS
#
#     return x
#
#
# def calc_center_y(row):
#     return row * (10 - consts.ROWS_OVERLAP) + \
#            consts.BUBBLE_RADIUS

def put_grass_in_grid():
    grass_list = []
    for num in range(20):
        line = random.randint(0, 21)
        column = random.randint(0, 49)
        while line == 0 and column == 0 or game_field[line][column]["number"] != Consts.FLAG_NUM:
            line = random.randint(0, 21)
            column = random.randint(0, 50)
            # check = (line, column)
        for l in range(column, column + 3):
            game_field[line][column]["number"] = Consts.GRASS_NUM
        Screen.pygame.transform(Consts.GRASS_IMG,
                                (game_field[line][column]["center_x"], game_field[line][column]["center_y"]))
        grass_list.append((line, column))
    return grass_list


def put_mines_in_grid():
    for num in range(20):
        line = random.randint(0, 21)
        column = random.randint(0, 49)
        while line == 0 and column == 0 or game_field[line][column]["number"] != Consts.FLAG_NUM:
            line = random.randint(0, 21)
            column = random.randint(0, 49)
        if game_field[line][column]["number"] == Consts.GRASS_NUM:
            game_field[line][num]["number"] = Consts.MINE_NUM
            pygame.surface.blit(Consts.MINE_IMG, Consts.GRASS_IMG,
                                (game_field[line][column]["center_x"], game_field[line][column]["center_y"]))
        mines_list.append([line, column])
        for l in range(column, column + 3):
            game_field[line][column]["number"] = Consts.MINE_NUM
    # mines_num = random.randint(1, len(put_grass_in_grid()))
    # for place in range(20):
    #     for num in range(mines_num):
    #         mines_place = random.randint(1, len(put_grass_in_grid()))
    #         mines_list.append(put_grass_in_grid()[mines_place])

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
                    tup = (row, column)
                    return tup


def soldier_location():
    soldier_slots = []
    for row in range(soldier_slot1()[0], soldier_slot1()[1] + 4):
        for column in range(soldier_slot1()[1], soldier_slot1()[1] + 1):
            soldier_slots.append((row, column))
    return soldier_slots


def should_soldier_pop():
    # if soldier_location()[-1]["number"] == Consts.MINE_NUM
    if soldier_location()[-1] in mines_list or soldier_location()[-2] in mines_list:
        return True
    return False


def flag_location():
    Screen.pygame.transform(Consts.FLAG_IMG, (21, 46))
    for row in range(21, 21 + 3):
        for column in range(46, 46 + 4):
            game_field[row][column]["number"] = Consts.FLAG_NUM


def touching_flag():
    if game_field[soldier_location()[-1][0]][soldier_location()[-1][1]]["number"] == Consts.FLAG_NUM and \
            game_field[soldier_location()[-2][0]][soldier_location()[-2][1]]["number"] == Consts.FLAG_NUM:
        return True
    return False
# for row in mines_list:
#     if  soldier_location()[-1][0] == row
#
# return len(same_color_cluster) >= consts.MIN_CLUSTER_SIZE_TO_POP
