import pygame
pygame.init()
screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
done = False
pcolor = pygame.Color(255,255,255)
screen.set_at((100,100),pcolor)
pygame.display.update()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

            pygame.quit()
