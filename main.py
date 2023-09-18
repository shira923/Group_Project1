import pygame
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
