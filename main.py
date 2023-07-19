import string

import pygame

import drawstars

done_executing = False


# Creates the main pygame window.
# screen_width: width of the window.
# screen_height: height of the window.
# screen_name: name of the window.
def main_window(screen_width: int, screen_height: int, screen_name: string):
    global done_executing
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(screen_name)
    # while done_executing hasn't been set to True,
    # we poll through pygame, checking for any events. in this case, checking if the application quit.
    # if the application did quit, then set done_executing to True, and quit.
    # otherwise, keep updating.
    while done_executing is False:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done_executing = True
                pygame.quit()
            # Run custom stuff!
            white = pygame.Color(255, 255, 255)
            drawstars.draw_stars(screen, white, 822, 153, 12)


# Creates a window with 800 width, 600 height.
main_window(1028, 768, "PYMath")
