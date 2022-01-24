import pygame
import Screens
import Constants


# import Entities


class Main:
    def __init__(self):
        # initialise game
        pygame.init()
        self.running = True
        self.Screens = Screens.StartScreen()
        self.window = pygame.display.set_mode(Constants.SIZE)
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
            print(self.running)
        pygame.quit()


main = Main()
main.game_loop()
