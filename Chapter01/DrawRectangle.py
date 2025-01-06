import pygame
pygame.init()
screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))

done = False

rectColor = pygame.Color(0,255,0)



def to_pygame_coordinates(display,x,y):
    return x, display.get_height()-y

position = to_pygame_coordinates(screen,100,600)
pygame.draw.rect(screen,rectColor,(position[0],position[1], 700, 200))

pygame.display.update()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done =True


            pygame.quit()
