import pygame

from pygame.locals import *

from OpenGL.GL import *

def pym_opengl_setup():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)