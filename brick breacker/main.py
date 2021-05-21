import pygame as pg
from settings import *
from sprite import *

class Game():
    def __init__(self):

        self.running = True
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(title)
        self.clock = pg.time.Clock()
        self.font_name = pg.font.match_font(FONT_NAME)

    def new(self):
        self.player1points = 0
        self.all_Sprites = pg.sprite.Group()
        self.players_group = pg.sprite.Group()
        self.ball_group = pg.sprite.Group()
        self.platform = pg.sprite.Group()

        self.player1 = Player1(self)
        self.all_Sprites.add(self.player1)
        self.players_group.add(self.player1)

        for plat in PLATFORM_LIST:
            p = Platform(self,*plat)
            self.all_Sprites.add(p)
            self.platform.add(p)



        for i in range(1):
            self.ball = Ball(self)
            self.all_Sprites.add(self.ball)
            self.ball_group.add(self.ball)

        self.run()

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

    def update(self):
        self.all_Sprites.update()


        hits = pg.sprite.collide_rect(self.player1,self.ball)
        if hits:
            self.ball.speedy *= -1
            self.ball.speedx *= 1
        hits = pg.sprite.spritecollide(self.ball,self.platform,True)
        if hits:
            self.ball.speedy *= -1
            self.player1points += 10

        if len(self.platform) < 1:
            self.draw_text("Next Level", 48, WHITE, WIDTH / 2, HEIGHT / 4)
            self.wait_for_key()
            self.new()




    def spawn_ball(self):
        for i in range(1):
            self.all_Sprites.add(self.ball)
            self.ball_group.add(self.ball)

    def draw(self):
        self.screen.fill(BLACK)
        self.draw_text("Score : "+str(self.player1points),20,WHITE,WIDTH-50,HEIGHT-30)



        self.all_Sprites.draw(self.screen)

        pg.display.flip()

    def show_title_screen(self):
        self.screen.fill(BLACK)
        self.draw_text(title, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Arrows to move", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press key to play", 14, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        if not self.running:
            return
        self.screen.fill(BLACK)
        self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score:" + str(self.player1points), 22, WHITE, WIDTH / 2, HEIGHT * 3 / 8)
        self.draw_text("Better luck nex time!", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("BY Jaxon Snow", 14, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
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