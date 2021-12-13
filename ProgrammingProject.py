import pygame
import screens

BLACK: (0,0,0)

class Main():
    def __init__(self):
        # initialise game
        pygame.init()
        self.running = True
        self.window = pygame.display.set_mode(300,300)
        self.screen = screens.Game_screen()
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
        pygame.display.flip()

    def gameloop(self):
        # game loop
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()

if __name__ == "__main__":
    game = Main()
    game.gameloop()
