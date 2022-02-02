import pygame
import Constants


# parent class that all other screen will inherit from
class Screen:
    def __init__(self):
        pass

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, window):
        pass


# creating the screen that will show upon opening the program:
class StartScreen(Screen):
    StartScreen = pygame.display.set_mode(Constants.SIZE)
    StartScreen.fill(Constants.WHITE)
    Ypos = 150
    for i in range(3):
        pygame.draw.rect(StartScreen, Constants.BLUE, [Constants.Xpos, Ypos, Constants.Bwidth, Constants.Bheight])
        Ypos = Ypos + 200
    pygame.display.flip()


class MainGame(Screen):
    pass


class Leaderboard(Screen):
    pass


class PauseMenu(Screen):
    pass
