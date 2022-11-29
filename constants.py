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

achismp144 = [(2, 1), (2, 2), (2, 27), (2, 28), (3, 1), (3, 2), (3, 27), (3, 28), (4, 19), (4, 20), (5, 18), (5, 21),
              (6, 19), (6, 20), (7, 15), (8, 14), (8, 16), (9, 13), (9, 17), (10, 13), (10, 16), (12, 13), (12, 16),
              (13, 12), (13, 16), (14, 13), (14, 15), (15, 14), (16, 9), (16, 10), (17, 8), (17, 11), (18, 9), (18, 10),
              (19, 1), (19, 2), (19, 27), (19, 28), (20, 1), (20, 2), (20, 27), (20, 28)]