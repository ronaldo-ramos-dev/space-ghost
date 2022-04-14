import pygame


class Explosion(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        super(Explosion, self).__init__()
        self.images = []

        for num in range(1,6):
            img = pygame.image.load(f"./assets/explosion/exp{num}.png")
            img = pygame.transform.scale(img, (100,100))
            self.images.append(img)

        self.index = 0
        self.surf = self.images[self.index]
        self.rect = self.surf.get_rect()
        self.rect.center = [x,y]
        self.counter = 0
        self.sound()


    def sound(self):
        sound = pygame.mixer.Sound("./assets/explosion/explosion.wav")
        channel = pygame.mixer.find_channel(True)
        channel.set_volume(0.4)
        channel.play(sound)



    def update(self):
        explosion_speed = 20
        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images) -1:
            self.counter = 0
            self.index += 1
            self.surf = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            print("kill")
            self.kill()
        