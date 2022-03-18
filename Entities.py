import random
import Constants
import pygame
import Screens


# character parent class
class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0, 0, 0, 0)

    def draw(self, window):
        window.blit(self.image, self.rect)

    def update(self):
        pass


# player character
class Player(Sprite):
    def __init__(self):
        super().__init__()
        # add player image
        self.image = pygame.Surface((35, 35))
        # self.image = pygame.image.load().convert()
        self.rect = self.image.get_rect()

    def update(self):
        # print(3) this is a test line
        # moving the player
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect = self.rect.move(0, -10)
        elif keys[pygame.K_s]:
            self.rect = self.rect.move(0, 10)
        elif keys[pygame.K_d]:
            self.rect = self.rect.move(10, 0)
        elif keys[pygame.K_a]:
            self.rect = self.rect.move(-10, 0)
        self.rect = self.rect.move(0, 5)
        # unless it is touching a platform the sprite will move downwards
        block_hit_list = pygame.sprite.spritecollide(Screens.MainGame.__init__(self).player,
                                                     Screens.MainGame.__init__(self).platforms, False)
        if block_hit_list[2]:
            self.rect = self.rect.move(0, 0)

    def reset(self):
        pass


# enemy character
class Enemy(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((35, 35))
        self.image.fill(Constants.RED)
        # Add enemy image
        self.rect = self.image.get_rect()
        self.rect.x = Constants.SIZE[0]
        self.rect.y = random.randint(420, 760)

    def update(self):
        self.rect = self.rect.move(-2, 0)


# platforms
class Platform(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 30))
        self.image.fill(Constants.BLUE)
        # Add enemy image
        self.rect = self.image.get_rect()
        self.rect.x = Constants.SIZE[0]
        self.rect.y = random.randint(450, 770)

    def update(self):
        self.rect = self.rect.move(-2, 0)
