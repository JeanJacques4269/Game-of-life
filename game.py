import numpy
import pygame.sprite
from constants import *
from grid import GameOfLife, MatGraphics
import pyperclip


class Game:
    def __init__(self, win, n=20):  # Here I put parameters related to when you generate the game, for example the map
        self.game_is_on = True
        self.win = win
        pattern = [(1, 2), (2, 2), (3, 2)]
        self.mat_of_life = GameOfLife(n, pattern)
        self.mat_of_life.update_neighbours()
        self.mat_front = MatGraphics(n, n)

    def run(self):
        while self.game_is_on:
            clock = pygame.time.Clock()
            dt = clock.tick(30)
            self.win.fill(BLACK)
            self.events()
            self.draw(self.win)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_is_on = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    self.mat_of_life.clear()
                elif event.key == pygame.K_s:
                    print("Copied : ", self.mat_of_life.get_pattern())
                    pyperclip.copy(str(self.mat_of_life.get_pattern()))
                else:
                    self.mat_of_life.next_day()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mat_front.handle(*event.pos, self.mat_of_life)

            if event.type == pygame.MOUSEMOTION:
                self.mat_front.update_focus(event.pos)

    def draw(self, win):
        self.mat_front.draw(win, self.mat_of_life)
        pygame.display.flip()
