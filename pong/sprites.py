import pygame as pg
import random as r
from os import path
from settings import *
vec = pg.math.Vector2

class Player1(pg.sprite.Sprite):
    def __init__(self,game):
        super(Player1, self).__init__()
        self.game = game
        self.image = pg.Surface((10, 75))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH-20,HEIGHT/2)



    def update(self):
        #movement
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_UP]:
            self.speedy = -.5*self.game.dt
        if keystate[pg.K_DOWN]:
            self.speedy = .5*self.game.dt
        self.rect.y += self.speedy
        #containment
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


class Player2(pg.sprite.Sprite):
    def __init__(self,game):
        super(Player2, self).__init__()
        self.game = game
        self.image = pg.Surface((10, 75))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (20,HEIGHT/2)



    def update(self):
        # movement
        self.speedy = 0
        keystate = pg.key.get_pressed()
        if keystate[pg.K_w]:
            self.speedy = -.5 * self.game.dt
        if keystate[pg.K_s]:
            self.speedy = .5 * self.game.dt
        self.rect.y += self.speedy
        # containment
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Ball(pg.sprite.Sprite):
    def __init__(self,game):
        super(Ball, self).__init__()
        self.game = game
        self.Player2 = Player2
        self.Player1 = Player1
        self.image = pg.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.speedx = .25
        self.speedy = .25



    def update(self):
        self.rect.x += self.speedx * self.game.dt
        self.rect.y += self.speedy * self.game.dt

        # if self.rect.top < 0:
        #     self.rect.top = 0
        # if self.rect.bottom > HEIGHT:
        #     self.rect.bottom = HEIGHT

        if self.rect.top <= 0:
            self.speedx *= 1
            self.speedy *= -1
        if self.rect.bottom >= HEIGHT:
            self.speedx *= 1
            self.speedy *= -1
        if self.rect.right >= WIDTH:
            self.speedx *= 1
            self.speedy *= -1
        if self.rect.left <= 0:
            self.speedx *= 1
            self.speedy *= -1

        if self.rect.right >= WIDTH:
            self.game.player2points+=1
            self.kill()
            self.game.spawn_ball()
            self.rect.center = (WIDTH / 2, HEIGHT / 2)

        if self.rect.left <= 0 :
            self.game.player1points+=1
            self.kill()
            self.game.spawn_ball()
            self.rect.center = (WIDTH / 2, HEIGHT / 2)



