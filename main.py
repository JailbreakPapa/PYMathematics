import pygame

# Creates the main pygame window.
# screen_width: width of the window.
# screen_height: height of the window.
def main_window(screen_width, screen_height):
    pygame.init()
    screen = pygame.display.set_mode((screen_width,screen_height))

main_window(800,600)