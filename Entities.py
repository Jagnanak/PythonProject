import pygame


# import Constants


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
        self.image = pygame.Surface((10, 10))
        # self.image = pygame.image.load().convert()
        self.rect = self.image.get_rect()

    def update(self):
        print(3)
        # self.rect = self.rect.move(10,1)
        self.rect.x = self.rect.x + 1

    def reset(self):
        pass


# enemy character
class Enemy(Sprite):
    def __init__(self):
        super().__init__()
        # Add enemy image
        self.rect = self.image.get_rect()
