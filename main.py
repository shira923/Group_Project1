import pygame
import os
import Consts
import Soldier


Soldier.soldier_movement(pygame)


def handle_player_events():
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

