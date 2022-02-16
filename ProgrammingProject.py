import pygame
import Screens
import Constants


# main game loop:
class Main:
    def __init__(self):
        # initialise game
        pygame.init()
        self.running = True
        self.screen = Screens.StartScreen()
        self.window = pygame.display.set_mode(Constants.SIZE)
        self.clock = pygame.time.Clock()

    def handle_events(self):
        # check input
        events = pygame.event.get()
        for event in events:
            # if quit
            if event.type == pygame.QUIT:
                self.running = False
            self.screen.handle_event(event)

    def update(self):
        self.screen.update()

    def draw(self):
        self.screen.draw(self.window)

    def game_loop(self):
        # game loop
        while self.running:
            if self.screen.nextScreen != None:
                self.screen = self.screen.nextScreen
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(Constants.FPS)
            # test code to check clock:
            # print(self.running)
        pygame.quit()


# calling the main game loop
main = Main()
main.game_loop()
