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

font = pygame.font.Font('Fonts/Graphic Stepfather.ttf',120)
font2 = pygame.font.Font('Fonts/Doonga Slash.ttf',60)
text = font.render('Ike Muoma', False, white)
text2 =font2.render('Hello world', False, green)



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #game loop code
    screen.blit(text, (10, 10))
    screen.blit(text2, (80, 100))
    pygame.display.update()

pygame.quit()