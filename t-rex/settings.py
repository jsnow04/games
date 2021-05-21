import pygame as pg
import random as r
from os import path


# colors (r,g,b)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
BROWN = (133, 79, 44)
ORANGE = (255, 98, 0)
PURPLE = (255, 0, 255)
PINK = (255, 0, 93)
LIGHT_BLUE = (18, 224, 218)
GREY = (149, 157, 161)
BG_COLOR = WHITE

WIDTH = 600
HEIGHT = 480
FPS = 60
title = "T-Rex Game"
FONT_NAME = 'arial'

PLAYER_GRAV = 0.8
PLAYER_JUMP = 12

PLATFORM_LIST = [(WIDTH/2,HEIGHT,WIDTH,30)]
SPAWN_TIME = [3000,1000,2000,500,]

ENEMY_IMG = []
ENEMY_LIST = ['cactus.jpg','cactus_short.jpg','bird.jpg']

game_folder = path.dirname(__file__)
imgs_folder = path.join(game_folder, "img")
snds_folder = path.join(game_folder, "snds")
trex_image = pg.image.load(path.join(imgs_folder,"t-rex.jpg"))
cactus_image = pg.image.load(path.join(imgs_folder,"cactus.jpg"))
trexdown = pg.image.load(path.join(imgs_folder,"trexduck.jpg"))
