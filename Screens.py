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
        if 90 < pos[1] < 90 + 150 and 600 < pos[0] < 900 and event.type == pygame.MOUSEBUTTONDOWN:
            self.nextScreen = MainGame()

    def update(self):
        pass

    def draw(self, window):
        window.fill(Constants.WHITE)
        pos = pygame.mouse.get_pos()
        Ypos = 90
        # drawing 3 buttons
        for i in range(3):
            if Ypos < pos[1] < Ypos + 150 and 600 < pos[0] < 900:
                pygame.draw.rect(window, Constants.RED, [Constants.Xpos, Ypos, Constants.Bwidth,
                                                         Constants.Bheight])
            else:
                pygame.draw.rect(window, Constants.BLUE, [Constants.Xpos, Ypos, Constants.Bwidth,
                                                          Constants.Bheight])
            Ypos = Ypos + 200


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
        window.fill(Constants.BLUE)
        self.player.draw(window)


class Leaderboard(Screen):
    def __init__(self):
        super().__init__()


class Tutorial(Screen):
    def __init__(self):
        super().__init__()


class PauseMenu(Screen):
    def __init__(self):
        super().__init__()
