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
        Ypos = 90
        # drawing 3 buttons
        for i in range(3):
            if Ypos < pos[1] < Ypos + 150 and 900 < pos[0] < 1200:
                pygame.draw.rect(window, Constants.RED, [Constants.X1pos, Ypos, Constants.B1width,
                                                         Constants.B1height])
            else:
                pygame.draw.rect(window, Constants.BLUE, [Constants.X1pos, Ypos, Constants.B1width,
                                                          Constants.B1height])
            Ypos = Ypos + 200
        # drawing text on the buttons


class MainGame(Screen):
    def __init__(self):
        super().__init__()
        self.player = Entities.Player()
        pygame.mouse.set_visible(False)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            quit()

    def update(self):
        self.player.update()

    def draw(self, window):
        window.fill(Constants.LIGHTGREY)
        self.player.draw(window)


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
        pygame.draw.rect(window, Constants.BLACK, [Constants.X2pos, Constants.Y2pos, Constants.B2width,
                                                   Constants.B2height])


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
        pygame.draw.rect(window, Constants.BLACK, [Constants.X2pos, Constants.Y2pos, Constants.B2width,
                                                   Constants.B2height])


class PauseMenu(Screen):
    def __init__(self):
        super().__init__()

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, window):
        pass
