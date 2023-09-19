import pygame
import Screen
import Consts
import GameField
import Soldier

# state = {
#     # "original_arrow": Screen.create_arrow(consts.ARROW_IMG),
#     # "rotated_arrow": None,
#     "is_bubble_fired": False,
#     "bubbles_popping": [],
#     # "turns_left_to_add_row": consts.NUM_OF_TURNS_TO_ADD_ROW,
#     "is_window_open": True,
#     # "state": consts.RUNNING_STATE,
#     "bullet_bubble": None,
#     "bubble_direction": None,
#     "mouse_angle": None
# }
running = True

def main():
    global running
    # pygame.display.flip()
    # GameField.create()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        GameField.create_game_field()
        GameField.put_grass_in_grid()
        GameField.put_mines_in_grid()
        Screen.make_screen()
        pygame.display.update()



    while True:
        # soldier_movement(y_change, x_change)
        handle_player_events()
        pygame.display.update()

main()


def handle_player_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
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

def soldier_movement(y_change, x_change):
    # y_change = 0
    # x_change = 0
    # while not GameField.should_soldier_pop() is True:
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
