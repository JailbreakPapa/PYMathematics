import pygame


def draw_stars(screen: pygame.display, starcolor: pygame.Color, x, y, size):
    pygame.draw.rect(screen, starcolor, (x, y, size, size))
