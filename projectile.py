import pygame

from pygame.locals import (
    RLEACCEL,
)


class Projectile(pygame.sprite.Sprite):

    def __init__(self, x,y):
        super(Projectile, self).__init__()
        self.surf = pygame.image.load("./assets/shoot/shoot.png").convert()
        self.surf.set_colorkey((255,255,255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.center = (x,y)
        self.speed = 5

    def update(self):
        self.rect.move_ip(self.speed, 0)

        if self.rect.bottom < 0:
            self.kill()