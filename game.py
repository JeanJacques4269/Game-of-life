import numpy
import pygame.sprite
from constants import *
from grid import GameOfLife, MatGraphics
import pyperclip


class Game:
    def __init__(self, win, n=50):
        self.game_is_on = True
        self.win = win
        pattern = achismp144
        self.mat_of_life = GameOfLife(n, pattern)
        self.mat_of_life.update_neighbours()
        self.mat_front = MatGraphics(n, n)

    def run(self):
        clock = pygame.time.Clock()
        while self.game_is_on:
            dt = clock.tick(FPS)
            self.win.fill(LIGHTBLACK)
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

            if event.type == pygame.MOUSEMOTION:
                self.mat_front.update_focus(event.pos)
        pressed = pygame.mouse.get_pressed(3)
        if pressed[0]:
            self.mat_front.handle_left(*pygame.mouse.get_pos(), self.mat_of_life)
        elif pressed[2]:
            self.mat_front.handle_right(*pygame.mouse.get_pos(), self.mat_of_life)

    def draw(self, win):
        self.mat_front.draw(win, self.mat_of_life)
        pygame.display.flip()
