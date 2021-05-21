import pygame as pg
from random import choice
from os import path
from settings import *
vec = pg.math.Vector2

class Sprite_sheet:
    def __init__(self,filename):
        self.spritesheet = pg.image.load(filename).convert()


    def get_image(self,x,y,width,height):
        image = pg.Surface((width,height))
        image.blit(self.spritesheet,(0,0), (x,y,width,height))
        image = pg.transform.scale(image,(width//2,height//2))
        return image


class Player(pg.sprite.Sprite):
    def __init__(self,game):
        self._layer = PLAYER_LAYER
        self.groups = game.all_Sprites
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.image = self.standing[0]
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
        self.pos = vec(40,HEIGHT-50)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def load_images(self):
        self.standing = [self.game.spritesheet.get_image(614,1063,120,191),
                         self.game.spritesheet.get_image(690,406,120,201)]
        for frame in self.standing:
            frame.set_colorkey(BLACK)
        self.walking_right = [self.game.spritesheet.get_image(678,860,120,201),
                              self.game.spritesheet.get_image(692,1458,120,207)]
        for frame in self.walking_right:
            frame.set_colorkey(BLACK)
        self.walking_left = []
        for frame in self.walking_right:
            self.walking_left.append(pg.transform.flip(frame,True,False))
        self.jump_frame = self.game.spritesheet.get_image(382,763,150,181)
        self.jump_frame.set_colorkey(BLACK)

    def jump_cut(self):
        if self.jumping:
            if self.vel.y <- 3:
                self.vel.y = -3

    def jump(self):
        # jump only if standing on a platform
        self.rect.x += 2
        hits = pg.sprite.spritecollide(self,self.game.platforms,False)
        self.rect.x -= 2
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -PLAYER_JUMP
            self.game.jump_sound.play()

    def update(self):
        self.animate()
        self.acc = vec(0,PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # motion
        self.vel += self.acc
        if abs(self.vel.x) <0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the screen
        if self.pos.x > WIDTH + self.rect.width/2:
            self.pos.x = 0 - self.rect.width/2
        if self.pos.x < 0 - self.rect.width/2:
            self.pos.x =  WIDTH + self.rect.width/2
        # position
        self.rect.midbottom = self.pos

    def animate(self):
        now = pg.time.get_ticks()
        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False
        # if self.vel.y!= 0:
        #     self.jumping = True
        # else:
        #     self.jumping = False

        if self.walking:
            if now - self.last_update >200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walking_left)
                bottom = self.rect.bottom
                if self.vel.x >0:
                    self.image = self.walking_right[self.current_frame]
                else:
                    self.image = self.walking_left[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

        # if self.jumping:
        #     if now -self.last_update > 200:
        #         self.last_update = now
        #         self.current_frame = (self.current_frame + 1) % len(self.jump_frame)
        #         bottom = self.rect.bottom
        #         self.rect = self.image.get_rect()
        #         self.rect.bottom = bottom
        if not self.jumping and not self.walking:
            if now - self.last_update> 360:
                self.last_update = now
                self.current_frame = (self.current_frame +1) % len(self.standing)
                bottom = self.rect.bottom
                self.image = self.standing[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom


class Platform(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self._layer = PLATFORM_LAYER
        self.groups = game.all_Sprites,game.platforms
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        images = [self.game.spritesheet.get_image(0,288,380,94),
                  self.game.spritesheet.get_image(213,1662,201,100)]
        self.image = choice(images)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        if r.randrange(100) < POW_SPAWN_PCT:
            Pow(self.game,self)

class Pow(pg.sprite.Sprite):
    def __init__(self,game,plat):
        self._layer = POW_LAYER
        self.groups = game.all_Sprites, game.powerups
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.plat = plat
        self.type = r.choice(['boost'])
        self.image = self.game.spritesheet.get_image(820,1805,71,70)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.plat.rect.centerx
        self.rect.bottom = self.plat.rect.top - 5

    def update(self):
        self.rect.bottom = self.plat.rect.top - 5
        if not self.game.platforms.has(self.plat):
            self.kill()

class Mob(pg.sprite.Sprite):
    def __init__(self,game):
        self._layer = MOB_LAYER
        self.groups = game.all_Sprites, game.mobs
        pg.sprite.Sprite.__init__(self,self.groups)
        self.game = game
        self.image_up = self.game.spritesheet.get_image(566,510,122,139)
        self.image_up.set_colorkey(BLACK)
        self.image_down = self.game.spritesheet.get_image(568,1534,122,135)
        self.image_down.set_colorkey(BLACK)
        self.image = self.image_up
        self.rect = self.image.get_rect()
        self.rect.centerx = choice([-100,WIDTH+100])
        self.vx = r.randrange(1,4)
        if self.rect.centerx>WIDTH:
            self.vx *= -1
        self.rect.y = r.randrange(HEIGHT/2)
        self.vy = 0
        self.dy = 0.5


    def update(self):
        self.rect.x += self.vx
        self.vy += self.dy
        if self.vy >3 or self.vy < -3:
            self.dy *=-1
        center = self.rect.center
        if self.dy <0:
            self.image = self.image_up
        else:
            self.image = self.image_down
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.rect.y += self.vy
        if self.rect.left > WIDTH + 100 or self.rect.right< -100:
            self.kill()