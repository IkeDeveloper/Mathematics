import pygame

pygame.init()
screen_width = 1200
screen_height = 1000
screen = pygame.display.set_mode((screen_width,
                                 screen_height))

done = False
white = pygame.Color(255, 255, 255)
green = pygame.Color(0,255,0)
pygame.font.init()

pygame.draw.polygon(screen, white,((150,200),(600,400),(400,600)))

pygame.display.update()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()