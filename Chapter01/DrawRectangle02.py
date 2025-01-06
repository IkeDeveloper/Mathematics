import pygame
import random
pygame.init()
screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

done = False

rectColor = pygame.Color(0,255,0)



def to_pygame_coordinates(display,x,y):
    return x, display.get_height()-y

for i in range(10):
    position = to_pygame_coordinates(screen,random.randrange(0,800),random.randrange(0,600))
    pygame.draw.rect(screen,rectColor,(position[0],position[1],random.randrange(0,100),random.randrange(0, 100)))

    pygame.display.update()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done =True

            pygame.quit()
