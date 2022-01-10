import pygame
import Constants


def screen_size(window):
    Constants.SIZE


class Screen:
    def __init__(self):
        pass

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def draw(self, window, screen_size):
        pass


class StartScreen(Screen):
    StartScreen = pygame.display.set_mode(Constants.SIZE)

class Leaderboard(Screen):
    pass



class PauseMenu(Screen):
    pass