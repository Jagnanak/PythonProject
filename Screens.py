import pygame
import Constants


class Screen:
    def __init__(self):
        pass

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, window):
        pass


class StartScreen(Screen):
    StartScreen = pygame.display.set_mode(Constants.SIZE)
    StartScreen.fill(Constants.WHITE)
    pygame.display.flip()


class MainGame(Screen):
    pass


class Leaderboard(Screen):
    pass


class PauseMenu(Screen):
    pass