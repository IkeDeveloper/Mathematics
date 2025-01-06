import math

import pygame

pygame.init()

timer = pygame.time.Clock()
fps =60

WIDTH = 1600
HEIGHT = 400

screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('side scroller')

background = pygame.image.load("bg.png")
background_width = background.get_width()
background = pygame.transform.scale(background,(background_width, HEIGHT))
#background_rect = background.get_rect()

scroll = 0
direction =0

panels = math.ceil(WIDTH/background_width)+2
run = True
while run:
    timer.tick(fps)
    for i in range(panels):
        screen.blit(background, (i * background_width + scroll-background_width,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_RIGHT:
                direction=1

            if event.key ==pygame.K_LEFT:
                direction=-1

        if event.type == pygame.KEYUP:
            if event.key ==pygame.K_RIGHT:
                direction=0

            if event.key ==pygame.K_LEFT:
                direction=0

    scroll -= 5 * direction
    if abs(scroll) > background_width:
        scroll = 0

    pygame.display.flip()
pygame.quit()

