import random
import Constants
import pygame
# import Screens


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
    def __init__(self, platforms):
        super().__init__()
        self.platforms = platforms
        # add player image
        self.image = pygame.Surface((35, 35))
        # self.image = pygame.image.load().convert()
        self.rect = self.image.get_rect()
        self.jump_time = 0
        self.currently_jumping = False

    def update(self):

        if self.currently_jumping:
            self.jump_time = self.jump_time + 1
            # print(self.jump_time)
            if self.jump_time > 30:
                self.currently_jumping = False

        block_hit_list = pygame.sprite.spritecollide(self, self.platforms, False)
        if block_hit_list:
            self.rect = self.rect.move(-Constants.GameSpeed, 0)
        # print(3) this is a test line
        # moving the player
        keys = pygame.key.get_pressed()
        jump_allowed = False
        self.rect = self.rect.move(0, Constants.GameSpeed)
        block_hit_list = pygame.sprite.spritecollide(self, self.platforms, False)
        if block_hit_list:
            self.rect = self.rect.move(0, -Constants.GameSpeed)
            jump_allowed = True
            self.jump_time = 0

        ymove = 0
        if keys[pygame.K_w] and (jump_allowed or self.currently_jumping):
            ymove = -15
            self.currently_jumping = True
        elif keys[pygame.K_s]:
            ymove = 15
        ymove = ymove + 5  # gravity
        self.rect = self.rect.move(0, ymove)
        # unless it is touching a platform the sprite will move downwards
        block_hit_list = pygame.sprite.spritecollide(self, self.platforms, False)
        if block_hit_list:
            self.rect = self.rect.move(0, -ymove)
        xmove = 0
        if keys[pygame.K_d]:
            xmove = 8
        elif keys[pygame.K_a]:
            xmove = -8
        self.rect = self.rect.move(xmove, 0)
        # unless it is touching a platform the sprite will move downwards
        block_hit_list = pygame.sprite.spritecollide(self, self.platforms, False)
        if block_hit_list:
            self.rect = self.rect.move(-xmove, 0)

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
        self.rect = self.rect.move(-Constants.GameSpeed, 0)


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
        self.rect = self.rect.move(-Constants.GameSpeed, 0)
