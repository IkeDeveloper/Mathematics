import pygame

from pygame.locals import *
from OpenGL.GL import *
from Mesh3D import*
mesh = Mesh3D()
pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF|OPENGL)
pygame.display.set_caption('OpenGL in Python')
done = False
white = pygame.Color(255,255,255)
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

mesh.draw()
pygame.display.flip()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()
