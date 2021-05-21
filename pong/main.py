import pygame as pg
from settings import *
from sprites import *

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



    def load_data(self):
        pass

    def new(self):
        self.player1points = 0
        self.player2points = 0
        self.all_Sprites = pg.sprite.Group()
        self.players_group = pg.sprite.Group()
        self.ball_group = pg.sprite.Group()


        self.player1 = Player1(self)
        self.player2 = Player2(self)
        self.ball = Ball(self)

        self.all_Sprites.add(self.player1)
        self.players_group.add(self.player1)
        self.all_Sprites.add(self.player2)
        self.players_group.add(self.player2)
        for i in range(1):
            self.all_Sprites.add(self.ball)
            self.ball_group.add(self.ball)


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



        hits = pg.sprite.collide_rect(self.ball,self.player1)
        if hits:
            self.ball.speedx *= -1
            self.ball.speedy *= 1
        hits = pg.sprite.collide_rect(self.ball, self.player2)
        if hits:
            self.ball.speedx *= -1
            self.ball.speedy *= 1


    def spawn_ball(self):
        for i in range(1):
            self.ball_group.add(self.ball)
            self.all_Sprites.add(self.ball)
        self.wait_for_key()

    def draw_text(self,text,size,color,x,y):
        font = pg.font.Font(self.font_name,size)
        text_surface = font.render(text,True,color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface,text_rect)


    def draw(self):
        self.screen.fill(BLACK)
        self.draw_text("Score:" +str(self.player1points),25,WHITE,WIDTH-50,15)
        self.draw_text("Score:" + str(self.player2points), 25, WHITE,50, 15)
        self.draw_text("PONG", 25, WHITE, WIDTH/2, 15)
        self.all_Sprites.draw(self.screen)

        pg.display.flip()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                if event.type == pg.KEYUP:
                    waiting = False
                    break


g = Game()
while g.running:
    g.wait_for_key()
    g.new()
    g.run()


pg.quit()