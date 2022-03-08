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
        self.image = pygame.Surface((35, 35))
        # self.image = pygame.image.load().convert()
        self.rect = self.image.get_rect()

    def update(self):
        print(3)
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
        # potential player movement code
        # self.rect.x = self.rect.y + 1

    def reset(self):
        pass


# enemy character
class Enemy(Sprite):
    def __init__(self):
        super().__init__()
        # Add enemy image
        self.rect = self.image.get_rect()
