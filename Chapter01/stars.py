import pygame
import random
pygame.init()
screen_width = 1200
screen_height = 1000
screen = pygame.display.set_mode((screen_width,screen_height))
done = False
pcolor = pygame.Color(255,255,255)
for i in range(1000):
    screen.set_at((random.randrange(0,screen_width),random.randrange(0,screen_height)),pcolor)

pygame.display.update()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()
