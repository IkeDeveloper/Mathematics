import pygame, sys, math
from pygame.locals import *

from Mathematics.Chapter01.Window import event


class Alieninvasion:

    def check_events(self, event):
        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def run_game(self):

        self.check_events(event)


class Mysprite(pygame.sprite.Sprite):
    def __init__(self, picture_path,pos_x,pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center =[pos_x, pos_y]

    def update(self):
        self.rect.center = pygame.mouse.get_pos()
        sprites.draw(screen)

class Playermissile(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x,pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]


    def update(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0]:
            if self.rect.x<screen_width:

                self.rect.x+=20
                self.rect.y=mouse_y
                pmissile.draw(screen)

            else:
                self.rect.x=mouse_x
        else:
            self.rect.x = mouse_x

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
        alien.draw(screen)



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

#Player missile sprite
pmissile = pygame.sprite.Group()
mymissile = Playermissile("SpriteImage/Fireball.png", pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1] )
pmissile.add(mymissile)

#Game loop

ai = Alieninvasion()
ai.run_game()


pygame.display.flip()
screen.fill((0, 0, 0))

#Player sprite
sprites.update()

# Alien paramters y_start,alienspeed,amplitude,sinstep
alien.update(00,2,500,0.01)

pmissile.update()

clock.tick(100)

