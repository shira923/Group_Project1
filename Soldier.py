import pygame
import Consts


def create_soldier():
    player_img = pygame.image.load(Consts.SOLDIER)
    player_height = 50
    player_width = 50
    player_img = pygame.transform.scale(player_img, (player_width, player_height))
    player_x, player_y = Consts.STARTING_POSITION


def soldier_out_of_borders(Main, Consts):
    player = Main.initiate_player()
    if player.rect.left < 0:
        player.rect.left = 0
    if player.rect.right > Consts.FIELD_ROWS:
        player.rect.right = Consts.FIELD_COLS
    if player.rect.top <= 0:
        player.rect.top = 0
    if player.rect.bottom >= Consts.FIELD_ROWS:
        player.rect.bottom = Consts.FIELD_ROWS

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