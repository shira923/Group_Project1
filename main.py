import pygame
import os
import GameField
import Soldier
import Consts

state = {
    "original_arrow": Screen.create_arrow(consts.ARROW_IMG),
    "rotated_arrow": None,
    "is_bubble_fired": False,
    "bubbles_popping": [],
    "turns_left_to_add_row": Consts.NUM_OF_TURNS_TO_ADD_ROW,
    "is_window_open": True,
    "state": Consts.RUNNING_STATE,
    "bullet_bubble": None,
    "bubble_direction": None,
    "mouse_angle": None
}



def main():
    pygame.init()
    GameField.create()

    while state["is_window_open"] and not GameField.should_soldier_pop():
        handle_user_events()

        if state["is_bubble_fired"]:

            move_soldier()












def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif state["state"] != Consts.RUNNING_STATE:
            continue

        if event.type == pygame.MOUSEMOTION:
            rotate_arrow()

        elif event.type == pygame.MOUSEBUTTONDOWN and \
                not state["is_bubble_fired"] and \
                not state["bubbles_popping"]:
            fire_bubble()


def soldier_movement(pygame):
    user_input = pygame.key.get_pressed()
    vel = 1
    x = 0
    y = 0
    if user_input == [pygame.K_LEFT]:
        x -= vel
    if user_input == [pygame.K_RIGHT]:
            x += vel
    if user_input == [pygame.K_UP]:
            y -= vel
    if user_input == [pygame.K_DOWN]:
        y += vel


class player(pygame.sprite):
    def initiate_player(Soldier, Consts, self):
       pygame.sprite.sprite.__inint__(self)
       self_images = []
       img = pygame.image.load(os.path.join('Group_Project1', Consts.SOLDIER_REG_IMAGE)).convert()
       self.images.append(img)
       self.image = self_images[Consts.STARTING_POSITION]
       self.rect = self.image.get_rect()





