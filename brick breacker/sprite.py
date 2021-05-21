import pygame as pg
import random as r
from os import path
from settings import *
vec = pg.math.Vector2

class Player1(pg.sprite.Sprite):
    def __init__(self,game):
        super(Player1, self).__init__()
        self.game = game
        self.image = pg.Surface((75, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT-20)


    def update(self):
        # movement
        self.speedx = 0

        keystate = pg.key.get_pressed()
        if keystate[pg.K_RIGHT]:
            self.speedx = .5 * self.game.dt
        if keystate[pg.K_LEFT]:
            self.speedx = -.5 * self.game.dt
        self.rect.x += self.speedx
        # containment
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

class Platform(pg.sprite.Sprite):
    def __init__(self,game,x,y,color):
        super(Platform, self).__init__()
        self.game = game
        self.image = pg.Surface((100,50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)


class Ball(pg.sprite.Sprite):
    def __init__(self,game):
        super(Ball, self).__init__()
        self.game = game
        self.Player1 = Player1
        self.image = pg.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.speedx = .25
        self.speedy = .25



    def update(self):
        #movement
        self.rect.x += self.speedx * self.game.dt
        self.rect.y += self.speedy * self.game.dt


        #containment
        if self.rect.right > WIDTH:
            self.speedx *= -1
        if self.rect.left < 0:
            self.speedx *= -1
        if self.rect.top < 0:
           self.speedy *= -1

        #kill
        if self.rect.bottom > HEIGHT:
            self.kill()
            self.game.playing = False

