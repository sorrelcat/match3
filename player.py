import pygame
import os
import constants as c

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'graphics')
player_img = pygame.image.load(os.path.join(img_folder, 'p1_jump.png'))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(c.BACKGROUND)
        self.rect = self.image.get_rect()
        self.rect.center = (c.WIDTH / 2, c.HEIGHT / 2)
        self.speedx = 0
        self.speedy = 0
        
    def update(self):
        self.speedx = 0
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -c.PLAYER_STEP
        if keystate[pygame.K_RIGHT]:
            self.speedx = c.PLAYER_STEP
        if keystate[pygame.K_UP]:
            self.speedy = -c.PLAYER_STEP
        if keystate[pygame.K_DOWN]:
            self.speedy = c.PLAYER_STEP
            
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
        if self.rect.right > c.WIDTH:
            self.rect.right = c.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        if 0 > self.rect.top:
            self.rect.top = 0  
        if self.rect.bottom > c.HEIGHT:
            self.rect.bottom = c.HEIGHT