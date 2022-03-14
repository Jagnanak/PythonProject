import pygame
import Constants
import Entities


# parent class that all other screen will inherit from
class Screen:
    def __init__(self):
        self.nextScreen = None

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, window):
        pass


# creating the screen that will show upon opening the program:
class StartScreen(Screen):
    def __init__(self):
        super().__init__()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            quit()
        pos = pygame.mouse.get_pos()
        if 90 < pos[1] < 90 + 150 and 900 < pos[0] < 1200 and event.type == pygame.MOUSEBUTTONDOWN:
            self.nextScreen = MainGame()
        elif 290 < pos[1] < 290 + 150 and 900 < pos[0] < 1200 and event.type == pygame.MOUSEBUTTONDOWN:
            self.nextScreen = Leaderboard()
        elif 490 < pos[1] < 490 + 150 and 900 < pos[0] < 1200 and event.type == pygame.MOUSEBUTTONDOWN:
            self.nextScreen = Tutorial()

    def update(self):
        pass

    def draw(self, window):
        window.fill(Constants.LIGHTGREY)
        pos = pygame.mouse.get_pos()
        ypos = 90
        # drawing 3 buttons
        for i in range(3):
            if ypos < pos[1] < ypos + 150 and 900 < pos[0] < 1200:
                pygame.draw.rect(window, Constants.RED, [Constants.X1pos, ypos, Constants.B1width,
                                                         Constants.B1height])
            else:
                pygame.draw.rect(window, Constants.BLUE, [Constants.X1pos, ypos, Constants.B1width,
                                                          Constants.B1height])
            ypos = ypos + 200

        # drawing text on the buttons
        # start button text
        font = pygame.font.Font('freesansbold.ttf', 64)
        text = font.render('START', True, Constants.BLACK)
        text_rect = text.get_rect()
        text_rect.center = (1050, 170)
        window.blit(text, text_rect)

        # leaderboard button text
        font = pygame.font.Font('freesansbold.ttf', 35)
        text = font.render('LEADERBOARD', True, Constants.BLACK)
        text_rect = text.get_rect()
        text_rect.center = (1050, 370)
        window.blit(text, text_rect)

        # tutorial button text
        font = pygame.font.Font('freesansbold.ttf', 40)
        text = font.render('HOW TO PLAY', True, Constants.BLACK)
        text_rect = text.get_rect()
        text_rect.center = (1050, 570)
        window.blit(text, text_rect)


class MainGame(Screen):
    def __init__(self):
        super().__init__()
        self.player = Entities.Player()
        self.platforms = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.delay = 0
        self.delay2 = 0
        pygame.mouse.set_visible(False)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            quit()

    def update(self):
        # randomly generating the platforms
        if self.delay == 45:
            newplatform = Entities.Platform()
            self.platforms.add(newplatform)
            self.delay = 0
        else:
            self.delay = self.delay + 1
        self.player.update()
        self.platforms.update()
        if pygame.sprite.spritecollide(self.player, self.platforms, False):
            print("touching")
        # randomly generating the enemies
        if self.delay2 == 250:
            newenemy = Entities.Enemy()
            self.enemies.add(newenemy)
            self.delay2 = 0
        else:
            self.delay2 = self.delay2 + 1
        self.enemies.update()
        if pygame.sprite.spritecollide(self.player, self.enemies, True):
            print("dead")

    def draw(self, window):
        window.fill(Constants.LIGHTGREY)
        self.player.draw(window)
        self.platforms.draw(window)
        self.enemies.draw(window)


class Leaderboard(Screen):
    def __init__(self):
        super().__init__()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            quit()
        pos = pygame.mouse.get_pos()
        if 20 < pos[1] < 60 and 20 < pos[0] < 80 and event.type == pygame.MOUSEBUTTONDOWN:
            self.nextScreen = StartScreen()

    def update(self):
        pass

    def draw(self, window):
        window.fill(Constants.LIGHTGREY)
        # back button
        pos = pygame.mouse.get_pos()
        if 20 < pos[1] < 60 and 20 < pos[0] < 80:
            pygame.draw.rect(window, Constants.BLACK, [Constants.X2pos, Constants.Y2pos, Constants.B2width,
                                                       Constants.B2height])
        else:
            pygame.draw.rect(window, Constants.DARKGREY, [Constants.X2pos, Constants.Y2pos, Constants.B2width,
                                                          Constants.B2height])
        # back button text
        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render('BACK', True, Constants.WHITE)
        text_rect = text.get_rect()
        text_rect.center = (50, 40)
        window.blit(text, text_rect)


class Tutorial(Screen):
    def __init__(self):
        super().__init__()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            quit()
        pos = pygame.mouse.get_pos()
        if 20 < pos[1] < 60 and 20 < pos[0] < 80 and event.type == pygame.MOUSEBUTTONDOWN:
            self.nextScreen = StartScreen()

    def update(self):
        pass

    def draw(self, window):
        window.fill(Constants.LIGHTGREY)
        # back button
        pos = pygame.mouse.get_pos()
        if 20 < pos[1] < 60 and 20 < pos[0] < 80:
            pygame.draw.rect(window, Constants.BLACK, [Constants.X2pos, Constants.Y2pos, Constants.B2width,
                                                       Constants.B2height])
        else:
            pygame.draw.rect(window, Constants.DARKGREY, [Constants.X2pos, Constants.Y2pos, Constants.B2width,
                                                          Constants.B2height])
        # back button text
        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render('BACK', True, Constants.WHITE)
        text_rect = text.get_rect()
        text_rect.center = (50, 40)
        window.blit(text, text_rect)


class PauseMenu(Screen):
    def __init__(self):
        super().__init__()

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, window):
        pass
