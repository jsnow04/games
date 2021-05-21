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
BG_COLOR = LIGHT_BLUE

WIDTH = 480
HEIGHT = 600
FPS = 60
title = "Template"
FONT_NAME = 'arial'
HS_FILE = "highscore.txt"
SPRITESHEET = "spritesheet_jumper.png"

#player properties
PLAYER_ACC= 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20

#game properties
BOOST_POWER = 60
POW_SPAWN_PCT = 7
MOB_FREQ = 5000
PLAYER_LAYER = 2
PLATFORM_LAYER = 1
POW_LAYER = 1
MOB_LAYER = 2
#starting plats

PLATFORM_LIST = [(0,HEIGHT - 50),
                 (WIDTH/2-50, HEIGHT * 3/4 - 50),
                 (125,HEIGHT-350),
                 (175,100),
                 (350,200)]


game_folder = path.dirname(__file__)
img_folder = path.join(game_folder,"imgs")
sound_folder = path.join(game_folder,"snds")