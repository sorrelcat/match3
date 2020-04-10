import pygame
import os
import random
import constants as c

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'graphics')
mob_img = pygame.image.load(os.path.join(img_folder, 'enemy.png'))

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = mob_img
        self.image.set_colorkey(c.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (c.WIDTH / 2, 0)
        self.speedx = 0
        self.speedy = 0
        
    def update(self):
        self.rect.x += c.MOB_STEP * random.randint(-1, 1)
        self.rect.y += c.MOB_STEP
        if self.rect.y == c.HEIGHT:
            self.rect.y = 0
            self.rect.h = c.WIDTH / 2