import pygame
import Constants
import Screens


class Button(Screens, Screens.StartScreen):
    pygame.draw.rect(Screens.StartScreen, Constants.BLUE, [30, 30, 30, 30])
    while pygame.mouse.get_pressed():
        if pygame.mouse.get_pos()[0] >= 30 and pygame.mouse.get_pos()[1] >= 30:
            pygame.draw.rect(Screens.StartScreen, Constants.RED, [30, 30, 30, 30])
