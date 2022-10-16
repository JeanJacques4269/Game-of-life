import pygame

from constants import *
from game import Game

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Game of life")
    win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    game = Game(win)
    game.run()
