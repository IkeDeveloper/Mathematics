import pygame

pygame.init()

screen_width = 1417
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('A cool lion')

done = False
background = pygame.image.load('image/lion.png')
sprite = pygame.image.load('image/Wolf.png')
screen.blit(background, (0,0))
screen.blit(sprite,(100,100))
pygame.display.update()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

            pygame.quit()
