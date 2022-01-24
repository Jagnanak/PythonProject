import pygame
# import Screens
import Constants
# import Entities


class Main:
    def __init__(self):
        # initialise game
        self.screen = None
        self.Screens = None
        pygame.init()
        self.running = True
        self.window = pygame.display.set_mode(Constants.SIZE)
        # add game screen
        self.clock = pygame.time.Clock()

    def handle_events(self):
        # check input
        events = pygame.event.get()
        for event in events:
            # if quit
            if event.type == pygame.QUIT:
                self.running = False
            self.Screens.handle_event(event)

    def update(self):
        self.Screens.update()

    def draw(self):
        self.Screens.draw(self.window)
        pygame.display.flip()

    def game_loop(self):
        # game loop
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(Constants.FPS)
        pygame.quit()
