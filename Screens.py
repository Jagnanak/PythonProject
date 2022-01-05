import pygame
import Constants


class Screen():
    def __init__(self):
        pass

    def handle_event(self, event):
        pass

    def screen_size(self, window):
        pygame.display.get_desktop_sizes()

    def update(self):
        pass

    def draw(self, window, screen_size):
        pass


class StartScreen(Screen):
    StartScreen = pygame.display.get_desktop_sizes()
    StartScreen.fill(Constants.WHITE)
    pygame.display.flip()


class Leaderboard(Screen):
    Leaderboard = pygame.display.get_desktop_sizes()
    Leaderboard.fill(Constants.WHITE)
    pygame.display.flip()


class PauseMenu(Screen):
    PauseMenu = pygame.display.get_desktop_sizes()
    PauseMenu.fill(Constants.WHITE)
    pygame.display.flip()
