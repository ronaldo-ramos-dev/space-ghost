import pygame
import random
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("./assets/meteor.png").convert_alpha()
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH+20,SCREEN_WIDTH+100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )

        self.speed = random.randint(1,3)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        
        if self.rect.right < 0:
            self.kill() 