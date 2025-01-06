# version 2.1
import math
import pygame
import random
pygame.init()

class Police:
    def __init__(self, x, y):

        self.img_path = "police_car.png"
        self.location = x, y
        self.draw()

    def draw(self):
         # load image and set its location
        self.img = pygame.image.load(self.img_path)
        self.img_location = self.img.get_rect()
        self.img_location.center = self.location

class EnemyCar:
    def __init__(self, x, y,z):
        image01= "greenCar.png"
        image02="truck_tractor01.png"
        image_list=[]
        image_list.append(image01)
        image_list.append(image02)

        self.img_path = image_list[z]
        self.location = x, y
        self.drawenemycar()

    def drawenemycar(self):
         # load image and set its location
        self.img = pygame.image.load(self.img_path)
        self.img_location = self.img.get_rect()
        self.img_location.center = self.location




def enemycar_randxpos():
    x=random.randint(300,750)
    return x

timer = pygame.time.Clock()
fps =60

WIDTH = 1000
HEIGHT = 1000
speed=0
acceleration=0.5
accelerationstep=0.04

screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('car game')

#background = pygame.image.load("2dRoad.jpg")
#background = pygame.image.load("road.png")
#background = pygame.image.load("road2.png")
background = pygame.image.load("concatenated_image.png")
background_height = background.get_height()
background = pygame.transform.scale(background,(WIDTH, background_height))
background_rect = background.get_rect()

mycar = pygame.sprite.Group()

scroll = 0
panels = math.ceil(HEIGHT/background_height)+2
run = True
xpos=600
enemy_ypos=0
enemy_ypos2=0
enemy_xpos=enemycar_randxpos()
enemy_xpos1=enemycar_randxpos()
carchoice=1
carchoice2=0
while run:
    timer.tick(fps)
    for i in range(panels):
        screen.blit(background, (0,i * background_height + scroll-background_height))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    scroll += speed + acceleration
    if acceleration<30:
        acceleration+=accelerationstep
    print(acceleration)
    if abs(scroll) > background_height:
        scroll = 0

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            xpos+=5

        if event.key == pygame.K_LEFT:
            xpos-=5
    playercar = Police(xpos, 700)


    #Responsible for enemy car 1
    enemy = EnemyCar(enemy_xpos,enemy_ypos,carchoice)

    #responsible for enemy car 2
    enemy1 =EnemyCar(enemy_xpos1,enemy_ypos2,carchoice2)

    enemy_ypos+=7
    enemy_ypos2+=10
    if enemy_ypos>1200:
        enemy_ypos=0
        enemy_xpos = enemycar_randxpos()
        carchoice = random.randint(0,1)

    if enemy_ypos2>1200:
        enemy_ypos2=0
        enemy_xpos1 = enemycar_randxpos()
        carchoice2 = random.randint(0, 1)

    screen.blit(playercar.img, playercar.img_location)
    screen.blit(enemy.img,enemy.img_location)
    screen.blit(enemy1.img,enemy1.img_location)
    pygame.display.flip()
pygame.quit()

#resizing page
#https://coderslegacy.com/python/how-to-resize-
