import random

import pygame
# import Constants


# character parent class
import Constants


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
        if keys[pygame.K_UP]:
            self.rect = self.rect.move(0, -10)
        elif keys[pygame.K_DOWN]:
            self.rect = self.rect.move(0, 10)
        elif keys[pygame.K_RIGHT]:
            self.rect = self.rect.move(10, 0)
        elif keys[pygame.K_LEFT]:
            self.rect = self.rect.move(-10, 0)
        # unless it is touching a platform the sprite will move downwards
        # self.rect = self.rect.move(0, 5)
        # potential player movement code
        # self.rect.x = self.rect.y + 1

    def reset(self):
        pass


# enemy character
class Enemy(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((35, 35))
        self.image.fill((255, 0, 0))
        # Add enemy image
        self.rect = self.image.get_rect()
        self.rect.x = Constants.SIZE[0]
        self.rect.y = random.randint(420, 760)

    def update(self):
        self.rect = self.rect.move(-2, 0)


# platform
class Platform(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 30))
        self.image.fill((0, 0, 255))
        # Add enemy image
        self.rect = self.image.get_rect()
        self.rect.x = Constants.SIZE[0]
        self.rect.y = random.randint(450, 780)

    def update(self):
        self.rect = self.rect.move(-2, 0)
