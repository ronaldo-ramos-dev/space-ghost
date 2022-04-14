from os import kill
from pickle import FALSE
import pygame
from player import Player
from enemy import Enemy
from explosion import Explosion
from settings import SCREEN_HEIGHT, SCREEN_WIDTH


from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    K_SPACE,
    KEYDOWN,
    QUIT,
)

def run():
    pygame.init()
    killed = False 
    clock = pygame.time.Clock()
    explosion_sound = pygame.mixer.Sound("./assets/explosion/explosion.wav")


    enemies = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    explosion_group = pygame.sprite.Group()
    projectile_group = pygame.sprite.Group()

    
    RUNNING = True

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 250)

    player = False
    killed = False
    
    pygame.mixer.music.load("./assets/music.ogg")
    pygame.mixer.music.play(loops=-1)   

    while RUNNING:

        if not player and not killed:
            player = Player()
            player_group.add(player)

        for event in pygame.event.get():
            if event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    RUNNING = False
                elif player and not killed and event.key == K_SPACE:
                    player.fire(all_sprites, projectile_group)

            elif event.type == pygame.QUIT:
                RUNNING = False

            elif event.type == ADDENEMY:
                new_enemy = Enemy()
                enemies.add(new_enemy)
                all_sprites.add(new_enemy)

            

        pressed_keys = pygame.key.get_pressed()

        if player:
            player.update(pressed_keys)

        enemies.update()

        screen.fill((0,0,0))

        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)

        if player:
            for player2 in player_group:
                screen.blit(player2.surf, player2.rect)

            
        if player:
            enemy_collided = pygame.sprite.spritecollide(player, enemies, True)

            if enemy_collided:
                pygame.mixer.Sound.play(explosion_sound)
                position = enemy_collided[0].rect.center
                explosion = Explosion(position[0], position[1])
                player_group.empty()
                player.kill()
                player = False
                killed = True
                explosion_group.add(explosion)
                all_sprites.add(explosion)

                # RUNNING = False
        
        fire_collided = pygame.sprite.groupcollide(projectile_group, enemies, True, True)
        
        if fire_collided:
            items = fire_collided.values()

            for item in items:
                item_exploded = item[0].rect.center
            
            explosion = Explosion(item_exploded[0], item_exploded[1])
            explosion_group.add(explosion)
            all_sprites.add(explosion)
            pygame.mixer.Sound.play(explosion_sound)



        explosion_group.update()
        projectile_group.update()

        pygame.display.flip()

        clock.tick(250)


    pygame.quit()




if __name__ == '__main__':
    run()    