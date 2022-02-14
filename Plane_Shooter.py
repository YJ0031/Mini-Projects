#Pygame imports
import pygame as py
from pygame.locals import *

#Other library imports
import random
import time
import math
import sys

class Player(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player = py.transform.scale( py.image.load("plane2.png").convert_alpha(), (64, 64))

        self.rect = self.player.get_rect()
        
        self.px = 20
        self.py = 20

        self.acc = 10

    def move(self):
        
        pressed_keys = py.key.get_pressed()

        if pressed_keys[K_UP]:
            self.rect.y -= self.acc
            if self.rect.y <= 20:
                self.rect.y = 20
        if pressed_keys[K_DOWN]:
            self.rect.y += self.acc
            if self.rect.y >= 350:
                self.rect.y = 350
        

class Coin(py.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        #self.coin = py.transform.scale(py.image.load("coin.png").convert(), (20, 20))

        self.coin = []
        self.rect = []
        self.y = [] #Stores the initial position of the coins
        self.count = 4 #Number of coins
        self.distance = 0
        self.pos_y = 340

        #self.rect = self.coin.get_rect()
        #self.rect.x = random.randint(1080, 1090)  
        #self.rect.y = random.randint(10, 390)

        for i in range(self.count):
            self.coin.append(py.transform.scale(py.image.load("coin.png").convert_alpha(), (30, 30)))

            self.rect.append(self.coin[i].get_rect())
            self.rect[i].x = 1090
            #while True:
            #if self.pos_y not in self.y:
            self.rect[i].y = self.pos_y
            self.y.append(self.rect[i].y)
            self.pos_y -= 100


        self.acc = 1

    def Move(self,coin):

        for i in range(self.count):
            self.rect[i].x -= self.acc


    def isCollision(self,no):
        global score_value
        #self.distance = px - cx
        #if self.distance < 50:
        #if self.rect[no].x < 0:
        #    return True
        #else:
        score_value += 1
        return True

class Debris(py.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.debris = []
        self.rect = []
        self.y = []
        self.count = 4 #Number of coins
        self.distance = 0
        self.pos_y = 340

        for i in range(self.count):
            self.debris.append(py.transform.scale(py.image.load("debris.png").convert_alpha(), (30, 30)))

            self.rect.append(self.debris[i].get_rect())
            
            self.rect[i].x = 1150
            
            
            self.rect[i].y = self.pos_y
            self.y.append(self.rect[i].y)
            self.pos_y -= 100
            
        self.acc = 1

    def Move(self, x, y, debris):

        for i in range(self.count):
            self.rect[i].x -= self.acc


    def isCollision(self,no):
        global score_value
        #self.distance = px - dx
        #if self.distance < 50:
        print(self.rect[no].x)
        #if self.rect[no].x < 0:
        #   return True
        #else:
        score_value -= 1
        return True        

class Score(py.sprite.Sprite):
    global font
    global screen
    def __init__(self, x, y):
        super().__init__()

        self.x = x
        self.y = y
    
    def display(self):
        global score_value
        global status
        if score_value < 0:
            status = True
        else:
            score = font.render("Score :" + str(score_value), True, (255, 255, 255))
            screen.blit(score, (self.x, self.y))
    
    def restart(self):

        global x, state, status, score_value, font, screen

        screen.fill((255, 255, 255))
        end_game = font.render ("Quit Game? Press Y or N.", True, (0, 0, 0))
        screen.blit(end_game, (340, 200))
        for event in py.event.get():
            if event.type == py.KEYDOWN:
                if event.key == py.K_y:
                    py.quit()
                    sys.exit()
                elif event.key == py.K_n:
                    x = 0

                    p = Player()

                    c = Coin()

                    d = Debris()

                    state = False
                    status = False

                    score_value = 0
                    font = py.font.Font('freesansbold.ttf', 32)

                    return "Done"


def main():
    global x
    global restart
    global s

    #Main loop
    while True:

        #Background
        rel_x = x % bg.get_rect().width
        screen.blit(bg, (rel_x - bg.get_rect().width, 0))
        if rel_x < Width:
            screen.blit(bg, (rel_x, 0))
            x -= 1

            #Player
            p.move()
            screen.blit(p.player,p.rect)

            #Coin
            for i in range(0,c.count):
                c.Move(c.coin[i])
                screen.blit(c.coin[i], c.rect[i])
                if c.rect[i].x < 40:
                    c.rect[i].x = 1090
                    c.rect[i].y = c.y[i]
                if c.rect[i].colliderect(p.rect):
                    state = c.isCollision(i)

                    if state == True:
                        c.rect[i].x = 1090
                        c.rect[i].y = c.y[i]

            #Debris

            for i in range(0,d.count):
                d.Move(d.rect[i].x, d.rect[i].y, d.debris[i])
                screen.blit(d.debris[i], d.rect[i])
                if d.rect[i].x < 40:
                    d.rect[i].x = 1090
                    d.rect[i].y = d.y[i]
                if p.rect.colliderect(d.rect[i]):
                    state = d.isCollision(i)

                    if state == True:
                        d.rect[i].x = 1090
                        d.rect[i].y = d.y[i]
            #Score

            s.display()

            if status != False:
                    stat = s.restart()
                    s = Score(10, 10)

                    if stat == "Done":
                        main()


            for event in py.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    py.quit()
                    sys.exit()


        py.display.update()
        py.display.flip()
        CLOCK.tick(FPS)

#Initialization
py.init()
Width = 1080
Height = 400
CLOCK = py.time.Clock()
screen = py.display.set_mode((Width, Height))
py.display.set_caption("Plane Game")
FPS = 30
background = py.image.load("cloud.png").convert()
bg = py.transform.scale(background, (Width, Height))
x = 0 #Variable for background movement

p = Player()

c = Coin()

d = Debris()

state = False
status = False

score_value = 0
font = py.font.Font('freesansbold.ttf', 32)

textx = 10
texty = 10

count = 0

s = Score(textx, texty)

#Calling the main loop of the game
main()

