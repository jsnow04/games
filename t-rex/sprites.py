import pygame as pg
import random as r
from os import path
from settings import *
vec = pg.math.Vector2

class Player1(pg.sprite.Sprite):
    def __init__(self,game):
        super(Player1, self).__init__()
        self.game = game
        self.image = trex_image
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.radius = self.rect.width * .75 / 2
        self.pos = vec(30, HEIGHT-50)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        # jump only if standing on a platform
        hits = pg.sprite.spritecollide(self, self.game.platform,False)
        if hits:
            self.vel.y = -PLAYER_JUMP

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        keystate = pg.key.get_pressed()
        if keystate[pg.K_SPACE]:
            self.jump()
        # motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the screen
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        # position
        self.rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self,x,y,w,h,c):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(c)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
class Mob(pg.sprite.Sprite):
    def __init__(self,game):
        super(Mob, self).__init__()
        self.num = r.randint(0,2)
        self.image = ENEMY_IMG[self.num]
        self.image.set_colorkey(BLACK)
        self.game = game
        if self.num == 1:
            self.rect = self.image.get_rect()
            self.radius = self.rect.width * .75 / 2
            self.rect.center = (WIDTH, HEIGHT - 45)
        if self.num == 2:
            self.rect = self.image.get_rect()
            self.radius = self.rect.width * .75 / 2
            self.h_list = [50,70,90]
            self.rect.center = (WIDTH, HEIGHT - r.choice(self.h_list))
        if self.num == 0:
            self.rect = self.image.get_rect()
            self.radius = self.rect.width * .75 / 2
            self.h_list = [50,70,90]
            self.rect.center = (WIDTH, HEIGHT - 55)



    def update(self):
        self.rect.x += -7

        #wrap around screen
        if self.rect.right <= 0:
            self.kill()
