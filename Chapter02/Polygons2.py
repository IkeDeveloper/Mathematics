from logging import DEBUG

import pygame
from pygame.locals import *

pygame.init()

screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

done = False
linecolor = pygame.Color(0, 255, 0)
timesClicked = 0
point3 =(0,0)
point4=(0,0)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            point1 = pygame.mouse.get_pos()
            point3=point1
            print(timesClicked)
            timesClicked +=1
        elif timesClicked==0:
            point2 = pygame.mouse.get_pos()
            point4=point2

        elif timesClicked==2:
            point5 = pygame.mouse.get_pos()
            triangle =[point3,point4,point5]
            print(timesClicked)
        elif timesClicked>2:
            pygame.draw.polygon(screen, linecolor, triangle)
            pygame.display.flip()
pygame.quit()