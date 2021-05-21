# ATTRIBUTION
# Code created by :Jaxon Snow
# Art created by:
# tutorial found at kidscancode.org






import pygame as pg
import random as r
from os import path
from settings import *
from sprites import *

class Game(object):

    def __init__(self):
        self.running = True
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()



    def load_data(self):
        # load high score
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir,'img')
        with open(path.join(self.dir, HS_FILE), 'w') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        self.spritesheet = Sprite_sheet(path.join(img_dir, SPRITESHEET))
        #sound
        self.snd_dir = path.join(self.dir,'snd')
        self.jump_sound = pg.mixer.Sound(path.join(self.snd_dir,'Jump33.wav'))
        self.pow_sound = pg.mixer.Sound(path.join(self.snd_dir, 'Boost16.wav'))

    def new(self):
        self.score = 0
        self.all_Sprites = pg.sprite.LayeredUpdates()
        self.platforms = pg.sprite.Group()
        self.powerups = pg.sprite.Group()
        self.players_group = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        # create game objects
        self.player = Player(self)

        # add objects to sprite groups
        self.players_group.add(self.player)
        for plat in PLATFORM_LIST:
            Platform(self,*plat)
        self.mob_timer = 0
        pg.mixer.music.load(path.join(self.snd_dir, 'Happy Tune.ogg'))
        #start running game loop
        self.run()

    def run(self):
        #game loop
        pg.mixer.music.play(loops=-1)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()
        pg.mixer.music.fadeout(500)



    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()
            if event.type == pg.KEYUP:
                if event.key == pg.K_SPACE:
                    self.player.jump_cut()

    def update(self):
        self.all_Sprites.update()

        #spawn mob
        now = pg.time.get_ticks()
        if now - self.mob_timer> 5000 +r.choice([-1000,-500,0,500,1000]):
            self.mob_timer = now
            Mob(self)

        mob_hits = pg.sprite.spritecollide(self.player,self.mobs,True)
        if mob_hits:
            self.playing = False

        # player hits plat fall
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player,self.platforms,False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.centery:
                        lowest = hit
                if self.player.pos.x -10 < lowest.rect.right and\
                        self.player.pos.x +10 > lowest.rect.left:
                    if self.player.pos.y < lowest.rect.centery:
                        self.player.pos.y = lowest.rect.top
                        self.player.vel.y = 0
                        self.player.jumping = False
        #if player reaches top 1/4 of screen
        if self.player.rect.top<=HEIGHT/4:
            for mob in self.mobs:
                mob.rect.y += max(abs(self.player.vel.y), 2)
            self.player.pos.y+= max(abs(self.player.vel.y),2)
            for plat in self.platforms:
                plat.rect.y +=max(abs(self.player.vel.y),2)

                if plat.rect.top > HEIGHT:
                    plat.kill()
                    self.score += 10

        #if player hits pow
        pow_hits= pg.sprite.spritecollide(self.player,self.powerups,True)
        for pow in pow_hits:
            if pow.type == 'boost':
                self.player.vel.y = -BOOST_POWER
                self.player.jumping = False
                self.pow_sound.play()

        if self.player.rect.bottom >HEIGHT:
            for sprite in self.all_Sprites:
                sprite.rect.y -= max(self.player.vel.y,10)
                if sprite.rect.bottom <0:
                    sprite.kill()
                if len(self.platforms) == 0:
                    self.playing = False
        # spawn plat

        while len(self.platforms) < 6:
            width = r.randrange(50,100)
            Platform(self,r.randrange(0,WIDTH-width),
                         r.randrange(-75,-30))

    def draw(self):
        self.screen.fill(BG_COLOR)
        self.all_Sprites.draw(self.screen)
        self.draw_text(str(self.score),22,WHITE,WIDTH/2,15)

        pg.display.flip()
    def show_title_screen(self):
        pg.mixer.music.load(path.join(self.snd_dir, 'Yippee.ogg'))
        pg.mixer.music.play(loops=-1)
        self.screen.fill(BG_COLOR)
        self.draw_text(title,48,BLACK,WIDTH/2,HEIGHT/4)
        self.draw_text("Arrows to move space to jump",22,BLACK,WIDTH/2,HEIGHT/2)
        self.draw_text("Press key to play",14,BLACK,WIDTH/2,HEIGHT*3/4)
        self.draw_text("High Score:" + str(self.highscore),22,BLACK,WIDTH/2,15)
        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)

    def show_go_screen(self):
        if not self.running:
            return
        pg.mixer.music.load(path.join(self.snd_dir, 'Yippee.ogg'))
        pg.mixer.music.play(loops=-1)
        self.screen.fill(BG_COLOR)
        self.draw_text("GAME OVER", 48, BLACK, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score:"+ str(self.score),22, BLACK,WIDTH/2,HEIGHT*3/8)
        self.draw_text("Better luck nex time!", 22, BLACK, WIDTH / 2, HEIGHT / 2)
        self.draw_text("BY Jaxon Snow", 14, BLACK, WIDTH / 2, HEIGHT * 3 / 4)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("Congratulations in a new high score!",22,BLACK,WIDTH/2,HEIGHT/2 + 40)
            with open(path.join(self.dir,HS_FILE), 'w')as f:
                f.write(str(self.score))
        else:
            self.draw_text("High Score:" + str(self.highscore),22,BLACK,WIDTH/2,HEIGHT/2 + 40)

        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False


    def draw_text(self,text,size,color,x,y):
        font = pg.font.Font(self.font_name,size)
        text_surface = font.render(text,True,color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface,text_rect)



g = Game()
g.show_title_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
