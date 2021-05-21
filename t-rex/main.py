import pygame as pg
from settings import *
from sprites import *
import random as r

class Game():
    def __init__(self):

        self.running = True
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()
        self.font_name = pg.font.match_font(FONT_NAME)
        self.load_data()
        self.total_mobs = r.randint(10,100)
        self.last_spawn = pg.time.get_ticks()
        self.spawn_delay = r.choice(SPAWN_TIME)

    def load_data(self):
        pass

    def new(self):
        self.score = 0
        self.all_Sprites = pg.sprite.Group()
        self.player_group = pg.sprite.Group()
        self.platform = pg.sprite.Group()
        self.npc_group = pg.sprite.Group()


        self.player = Player1(self)

        self.all_Sprites.add(self.player)
        self.player_group.add(self.player)
        p = Platform(0,HEIGHT-30,WIDTH,30,WHITE)
        self.all_Sprites.add(p)
        self.platform.add(p)
        p = Platform(0,HEIGHT-30,WIDTH,2,BLACK)
        self.all_Sprites.add(p)
        self.platform.add(p)
        self.spawn_mob()
        self.run()

    def spawn_mob(self):
        self.total_mobs -=1
        self.score +=10
        for img in ENEMY_LIST:
            ENEMY_IMG.append(pg.image.load(path.join(imgs_folder,img)).convert())
        for i in range(1):
            npc = Mob(self)
            self.all_Sprites.add(npc)
            self.npc_group.add(npc)
            self.spawn_delay = r.choice(SPAWN_TIME)


    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    self.player.image = trexdown
                    self.player.rect = self.player.image.get_rect()
                    self.player.image = pg.transform.scale(trexdown,(50,30))
            if event.type == pg.KEYUP:
                if event.key == pg.K_DOWN:
                    self.player.image = trex_image
                    self.player.rect = self.player.image.get_rect()
                    self.player.image = pg.transform.scale(trex_image, (30, 50))

    def update(self):
        self.all_Sprites.update()

        now = pg.time.get_ticks()
        if (now - self.last_spawn) > self.spawn_delay:
            self.last_spawn = now
            if self.total_mobs >= 0:
                self.spawn_mob()
            if self.total_mobs <= 0:
                self.total_mobs += r.randint(10,100)


        hits = pg.sprite.spritecollide(self.player,self.platform,False)
        if hits:
            self.player.pos.y = hits[0].rect.top
            self.player.vel.y = 0

        if self.player.rect.bottom >= HEIGHT:
            self.player.kill()
            self.playing = False
        hits = pg.sprite.spritecollide(self.player,self.npc_group,False)
        if hits:
            for sprite in self.all_Sprites:
                sprite.kill()
            self.playing = False




    def draw(self):
        self.screen.fill(WHITE)
        self.all_Sprites.draw(self.screen)
        self.draw_text(str(self.score),22,BLACK,WIDTH/2,15)

        pg.display.flip()

    def show_title_screen(self):
        self.screen.fill(BG_COLOR)
        self.draw_text(title,48,BLACK,WIDTH/2,HEIGHT/4)
        self.draw_text("Space to jump",22,BLACK,WIDTH/2,HEIGHT/2)
        self.draw_text("Press key to play",14,BLACK,WIDTH/2,HEIGHT*3/4)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        if not self.running:
            return
        self.screen.fill(BG_COLOR)
        self.draw_text("GAME OVER", 48, BLACK, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score:"+ str(self.score),22, BLACK,WIDTH/2,HEIGHT*3/8)
        self.draw_text("Better luck nex time!", 22, BLACK, WIDTH / 2, HEIGHT / 2)
        self.draw_text("BY Jaxon Snow", 14, BLACK, WIDTH / 2, HEIGHT * 3 / 4)


        pg.display.flip()
        self.wait_for_key()

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