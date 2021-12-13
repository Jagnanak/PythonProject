import pygame


class Screen():
    def __init__(self):
        pass

    def handle_event(self, event):
        pass

    def Screen_Size(self, window):
        pygame.display.get_desktop_sizes()

    def update(self):
        pass

    def draw(self, window, Screen_Size):
        pass


class Start_Screen(Screen):
    pass


class Leaderboard(Screen):
    pass


class Pause_Menu(Screen):
    pass
