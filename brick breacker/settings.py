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

WIDTH = 600
HEIGHT = 480
FPS = 60
title = "Breaker"
FONT_NAME = 'arial'

PLATFORM_LIST = [(50,25,RED),
                 (50,75,BLUE),
                 (50,125,YELLOW),
                 (50,175,PINK),
                 (150, 25,PINK),
                 (150, 75,RED),
                 (150, 125,BLUE),
                 (150, 175,YELLOW),
                 (250, 25,YELLOW),
                 (250, 75,PINK),
                 (250, 125,RED),
                 (250, 175,BLUE),
                 (350, 25,BLUE),
                 (350, 75,YELLOW),
                 (350, 125,PINK),
                 (350, 175,RED),
                 (450, 25,RED),
                 (450, 75,BLUE),
                 (450, 125,YELLOW),
                 (450, 175,PINK),
                 (550, 25, PINK),
                 (550, 75, RED),
                 (550, 125, BLUE),
                 (550, 175, YELLOW)
                 ]


