import pygame, sys, random

class Mysprite(pygame.sprite.Sprite):
    def __init__(self, picture_path,pos_x,pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center =[pos_x, pos_y]

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Aliensprite(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
    def update(self):
        self.rect.x-=5

pygame.init()
clock = pygame.time.Clock()

screen_width = 1920
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Graphic example')
pygame.mouse.set_visible(False)

#Player sprite
sprites = pygame.sprite.Group()
playersprite = Mysprite("SpriteImage/manSprite.gif",500,500)
sprites.add(playersprite)

#Alien sprite
alien = pygame.sprite.Group()
enemysprite = Aliensprite("SpriteImage/egg3.png",1900, random.randrange(0,screen_height-200))
alien.add(enemysprite)


#Game loop
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    screen.fill((0, 0, 0))

    sprites.draw(screen)
    sprites.update()

    alien.draw(screen)
    alien.update()

    clock.tick(60)
