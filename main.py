import pygame
import random
import os

WIDTH = 360  
HEIGHT = 480 
FPS = 30 
PLAYER_STEP = 2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BACKGROUND = (76, 105, 113)

pygame.init()
pygame.mixer.init()  
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Match 3")
clock = pygame.time.Clock()

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'graphics')
player_img = pygame.image.load(os.path.join(img_folder, 'p1_jump.png')).convert()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(BACKGROUND)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        
    def update(self):
        self.rect.x += random.randint(-PLAYER_STEP, PLAYER_STEP)
        self.rect.y += random.randint(-PLAYER_STEP, PLAYER_STEP)
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        if 0 > self.rect.top:
            self.rect.top = 0  
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running = True

while running:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    all_sprites.update()
    screen.fill(BLACK)
    
    all_sprites.draw(screen)
    pygame.display.flip()