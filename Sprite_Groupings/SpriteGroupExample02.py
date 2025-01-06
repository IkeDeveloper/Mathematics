import pygame, sys, math
class Mysprite(pygame.sprite.Sprite):
    def __init__(self, picture_path,pos_x,pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center =[pos_x, pos_y]

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Aliensprite(pygame.sprite.Sprite):
    def __init__(self,picture_path, pos_x):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x,1000]
        self.sinstep=0

    def update(self,y_start,alienspeed,amplitude,sinstep):
        self.rect.x-=alienspeed
        self.sinstep += sinstep
        self.sinstep %= 2 * math.pi
        self.rect.y= (1 * math.sin(self.sinstep) * amplitude)+y_start

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
enemysprite = Aliensprite("SpriteImage/egg3.png",1900)
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


    # Alien paramters y_start,alienspeed,amplitude,sinstep

    alien.update(500,2,200,0.01)
    alien.draw(screen)
    alien.update(800,2,800,0.01)
    alien.draw(screen)

    clock.tick(60)
