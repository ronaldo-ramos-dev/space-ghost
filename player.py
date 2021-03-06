import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, PLAYER_SPEED
from projectile import Projectile

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



class Player(pygame.sprite.Sprite):
    
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("./assets/spaceghost.png").convert()
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect()

    def fire(self, group_sprite, projectile_group):
        projectile = Projectile(self.rect.center[0], self.rect.center[1])
        group_sprite.add(projectile)
        projectile_group.add(projectile)
        SHOOT_SOUND = pygame.mixer.Sound("./assets/shoot/shoot.wav")
        channel=pygame.mixer.find_channel(True)
        channel.set_volume(0.4)
        channel.play(SHOOT_SOUND)

    def update(self, pressed_keys):

        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

            

