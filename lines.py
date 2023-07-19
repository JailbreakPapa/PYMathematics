import pygame

import string

from pygame import MOUSEBUTTONDOWN


# Creates a line using Cartesian Coordinates.
# in a standard math way, a line is represented like this:
# Y = MX + C (M: Slope, C: Y-Intercept)
def create_line(line_color: pygame.Color, mouse_point1: tuple[int, int], mouse_point2: tuple[int, int],
                screen: pygame.Surface):
    pygame.draw.line(screen, line_color, mouse_point1, mouse_point2, 1)


