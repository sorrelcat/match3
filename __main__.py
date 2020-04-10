import pygame
import os
import random

import player, mob 
import constants as c

pygame.init()
pygame.mixer.init()  

screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
pygame.display.set_caption("UFO")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = player.Player()
mob = [mob.Mob()]
all_sprites.add(player)
all_sprites.add(mob)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'graphics')
background = pygame.image.load(os.path.join(img_folder, 'starfield.png')).convert()
background_rect = background.get_rect()

running = True

while running:
    clock.tick(c.FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False     
    
    all_sprites.update()
    screen.blit(background, background_rect)
    
    all_sprites.draw(screen)
    pygame.display.flip()
    
    if pygame.sprite.spritecollide(player, mob, False):
        running = False