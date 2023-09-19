import pygame
import Screen
import Consts
import GameField
import Soldier

# state = {
#     "original_arrow": Screen.create_arrow(consts.ARROW_IMG),
#     "rotated_arrow": None,
#     "is_bubble_fired": False,
#     "bubbles_popping": [],
#     "turns_left_to_add_row": consts.NUM_OF_TURNS_TO_ADD_ROW,
#     "is_window_open": True,
#     "state": consts.RUNNING_STATE,
#     "bullet_bubble": None,
#     "bubble_direction": None,
#     "mouse_angle": None
# }

state["rotated_arrow"] = state["original_arrow"]


# def main():
#     pygame.init()
#     GameField.create()
#
#     while state["is_window_open"]:
#
#         handle_user_events()
#
#         if state["is_bubble_fired"]:
#
#             move_bubble()
#
#             if Bubble.should_stop(BubblesGrid.bubbles_grid,
#                                   state["bullet_bubble"]):
#                 state["is_bubble_fired"] = False
#
#                 new_bubble_location = BubblesGrid.find_bubble_location_in_grid(
#                         state["bullet_bubble"])
#                 BubblesGrid.put_bubble_in_grid(state["bullet_bubble"],
#                                                new_bubble_location)
#
#                 same_color_cluster = BubblesGrid.get_same_color_cluster(
#                         new_bubble_location,
#                         state["bullet_bubble"]["color"],
#                         [])
#
#                 if BubblesGrid.should_bubbles_pop(same_color_cluster):
#                     state["bubbles_popping"] = \
#                         BubblesGrid.pop_bubbles(same_color_cluster)
#
#                 # The counter counts only if bubbles weren't popped
#                 else:
#                     state["turns_left_to_add_row"] -= 1
#
#                     if state["turns_left_to_add_row"] == 0:
#                         BubblesGrid.add_new_line()
#
#                         # Reseting the counter
#                         state["turns_left_to_add_row"] = \
#                             consts.NUM_OF_TURNS_TO_ADD_ROW
#
#                 remove_isolated_bubbles()
#                 BubblesGrid.set_one_empty_line()
#                 remove_extinct_colors(consts.bubble_colors)
#                 Stack.add_bubble(Stack.get_length())
#
#                 if is_lose():
#                     state["state"] = consts.LOSE_STATE
#                 elif is_win():
#                     state["state"] = consts.WIN_STATE
#
#         Screen.draw_game(state)


# def handle_user_events():
#     for event in pygame.event.get():
#
#         if event.type == pygame.QUIT:
#             state["is_window_open"] = False
#
#         elif state["state"] != consts.RUNNING_STATE:
#             continue
#
#         if event.type == pygame.MOUSEMOTION:
#             rotate_arrow()
#
#         elif event.type == pygame.MOUSEBUTTONDOWN and \
#                 not state["is_bubble_fired"] and \
#                 not state["bubbles_popping"]:
#             fire_bubble()

#
# def rotate_arrow():
#     state["mouse_angle"] = Screen.calc_mouse_angle(pygame.mouse.get_pos())
#     state["rotated_arrow"] = pygame.transform.rotate(state["original_arrow"],
#                                                      state["mouse_angle"] - 90)
#
#
# def fire_bubble():
#     state["is_bubble_fired"] = True
#     state["bubble_direction"] = \
#         Bubble.calc_direction(state["mouse_angle"])
#     state["bullet_bubble"] = Stack.remove_first()
#
#
# def move_bubble():
#     Bubble.move_in_direction(state["bullet_bubble"], state["bubble_direction"])
#
#     if Bubble.is_colliding_with_wall(state["bullet_bubble"]):
#         state["bubble_direction"] = (state["bubble_direction"][0] * (-1),
#                                      state["bubble_direction"][1])
#
#
# def remove_isolated_bubbles():
#     isolated_bubbles_locations = BubblesGrid.find_isolated_bubbles()
#
#     if len(isolated_bubbles_locations) > 0:
#         state["bubbles_popping"] += \
#             BubblesGrid.pop_bubbles(isolated_bubbles_locations)
#

def handle_player_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("Player moved up!")
            elif event.key == pygame.K_DOWN:
                print("Player moved down!")
            elif event.key == pygame.K_LEFT:
                print("Player moved left!")
            elif event.key == pygame.K_RIGHT:
                print("Player moved right!")


# Soldier.soldier_movement(pygame)

def soldier_movement():
    y_change = 0
    x_change = 0
    while not GameField.should_soldier_pop() == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change -= Consts.SOLDIER_MOVEMENT_AMOUNT
                elif event.key == pygame.K_DOWN:
                    y_change += Consts.SOLDIER_MOVEMENT_AMOUNT
                if event.key == pygame.K_LEFT:
                    x_change -= Consts.SOLDIER_MOVEMENT_AMOUNT
                    if event.key == pygame.K_RIGHT:
                        x_change += Consts.SOLDIER_MOVEMENT_AMOUNT
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
                elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        Consts.X_SOLDIER = x_change
        Consts.Y_SOLDIER = y_change
        return Consts.X_SOLDIER, Consts.Y_SOLDIER





handle_player_events()
