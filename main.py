import pygame
import os
import Soldier
import Consts
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


