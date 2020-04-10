import pygame
import os
import random

import player 
import constants as c

pygame.init()
pygame.mixer.init()  

screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
pygame.display.set_caption("UFO")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = player.Player()
all_sprites.add(player)

running = True

while running:
    clock.tick(c.FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False            
    
    all_sprites.update()
    screen.fill(c.BLACK)
    
    all_sprites.draw(screen)
    pygame.display.flip()