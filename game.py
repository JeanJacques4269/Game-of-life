import numpy
import pygame.sprite
from constants import *
from grid import GameOfLife


class Game:
    def __init__(self, win, n=5):  # Here I put parameters related to when you generate the game, for example the map
        self.game_is_on = True
        self.win = win
        l = [(1, 2), (2, 2), (3, 2)]
        self.mat_of_life = GameOfLife(n, l)

    def run(self):
        while self.game_is_on:
            clock = pygame.time.Clock()
            dt = clock.tick(5)
            self.win.fill(BLACK)
            self.events()
            self.draw(self.win)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if you push the red cross, it close the game
                self.game_is_on = False
            if event.type == pygame.KEYDOWN:
                self.mat_of_life.next_day()
        # end of default code

    def draw(self, win):
        self.mat_of_life.draw(win)
        pygame.display.flip()
