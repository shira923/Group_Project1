import pygame
import Screen
import Consts
import GameField
import Soldier

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


Soldier.soldier_movement(pygame)
handle_player_events()
