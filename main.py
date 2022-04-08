from pickle import FALSE
import pygame
from player import Player
from enemy import Enemy
from settings import SCREEN_HEIGHT, SCREEN_WIDTH


from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

def run():
    pygame.init()

    clock = pygame.time.Clock()

    enemies = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    
    RUNNING = True

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 250)

    player = Player()

    all_sprites.add(player)

    pygame.mixer.music.load("./assets/music.ogg")
    pygame.mixer.music.play(loops=-1)   

    while RUNNING:

        for event in pygame.event.get():
            if event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    RUNNING = False

            elif event.type == pygame.QUIT:
                RUNNING = False

            elif event.type == ADDENEMY:
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

        pressed_keys = pygame.key.get_pressed()

        player.update(pressed_keys)

        enemies.update()

        screen.fill((0,0,0))

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        if pygame.sprite.spritecollideany(player, enemies):
            player.kill()
            RUNNING = False

        pygame.display.flip()

        clock.tick(250)


    pygame.quit()




if __name__ == '__main__':
    run()    