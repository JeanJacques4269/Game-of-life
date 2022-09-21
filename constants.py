import platform
from colors import *
import pygame.math
from screeninfo import get_monitors

WIDTH, HEIGHT = 1920, 1080
ratio = 3 / 4  # corresponds to the place I want my window to take. For example, 1 will be fullscreen.
WIDTH, HEIGHT = int(WIDTH * ratio), int(HEIGHT * ratio)

G_SIZE = 500
LEFT = (WIDTH - G_SIZE) / 2
TOP = (HEIGHT - G_SIZE) / 2

# game
FPS = 60
