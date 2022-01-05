import pygame
import Constants


class Sprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0, 0, 0, 0)

    def draw(self, window):
        window.blit(self.image, self.rect)

    def update(self):
        pass


class Player(Sprite):
    def __init__(self):
        super().__init__()
        # add player image
        # self.image = pygame.image.load().convert()
        self.rect = self.image.get_rect()

    def update(self):
        pass

    def reset(self):
        pass
