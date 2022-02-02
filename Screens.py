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
    start = True
    StartScreen = pygame.display.set_mode(Constants.SIZE)
    StartScreen.fill(Constants.WHITE)
    # button code:
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            pos = pygame.mouse.get_pos()
            Ypos = 90
            for i in range(3):
                if Ypos < pos[1] < Ypos + 150 and 600 < pos[0] < 900:
                    pygame.draw.rect(StartScreen, Constants.RED, [Constants.Xpos, Ypos, Constants.Bwidth, Constants.Bheight])
                    Ypos = Ypos + 200
                else:
                    pygame.draw.rect(StartScreen, Constants.BLUE, [Constants.Xpos, Ypos, Constants.Bwidth, Constants.Bheight])
                    Ypos = Ypos + 200
            pygame.display.flip()
    pygame.display.flip()

# if needed
    # Ypos = 150
    # for i in range(3):
    # Ypos = Ypos + 200


class MainGame(Screen):
    pass


class Leaderboard(Screen):
    pass


class PauseMenu(Screen):
    pass
