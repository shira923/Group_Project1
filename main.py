import pygame
import os
import Consts
import Soldier


Soldier.soldier_movement(pygame)


def handle_player_events():
    for event in pygame.event.get():
        if event.type == pygame.pygame.KEYDOWN:

