import itertools
import math

import numpy
import pygame.draw
from constants import *


def matrice(n):
    return numpy.zeros((n, n), dtype=int)


def neighbours(i, j, n):
    res = []
    directions = list(itertools.product((-1, 0, 1), (-1, 0, 1)))
    for e in directions:
        ni, nj = i + e[0], j + e[1]
        if 0 <= ni < n and 0 <= nj < n:
            res.append((ni, nj))
    res.remove((i, j))
    return res


class MatGraphics:
    def __init__(self, n, m):
        self.mat = [[0 for _ in range(m)] for _ in range(n)]
        self.n, self.m = n, m
        self.focused = None
        self.CASE_SIZE = int(G_SIZE / n)

    def draw(self, win, matmat):
        self.n = self.n
        pygame.draw.rect(win, BLACK,
                         pygame.rect.Rect(LEFT - 4, TOP - 4, self.CASE_SIZE * self.n + 4, self.CASE_SIZE * self.n + 4),
                         1)
        matmat.draw(win)
        if self.focused:
            size = self.CASE_SIZE
            i, j = self.focused
            y, x = i * size, j * size
            pygame.draw.rect(win, GRAY,
                             pygame.rect.Rect(LEFT + x, TOP + y, size * 1, size * 1),
                             int(1 + math.log(1 + 50 / self.n)))

    def update_focus(self, pos):
        n = self.n
        self.focused = None
        x, y = pos
        j = (x - LEFT) // self.CASE_SIZE
        i = (y - TOP) // self.CASE_SIZE
        if 0 <= i < n and 0 <= j < n:
            self.focused = i, j

    def handle_left(self, x, y, matoflife):
        j = int((x - LEFT) // self.CASE_SIZE)
        i = int((y - TOP) // self.CASE_SIZE)
        n = self.n
        if 0 <= i < n and 0 <= j < n:
            matoflife.mat[i, j] = 1
            matoflife.update_neighbours()

    def handle_right(self, x, y, matoflife):
        j = int((x - LEFT) // self.CASE_SIZE)
        i = int((y - TOP) // self.CASE_SIZE)
        n = self.n
        if 0 <= i < n and 0 <= j < n:
            matoflife.mat[i, j] = 0
            matoflife.update_neighbours()


class GameOfLife:
    def __init__(self, n, pat):
        self.n = n
        self.mat = matrice(n)
        self.voisins = matrice(n)
        for e in pat:
            self.mat[e] = 1
        self.CASE_SIZE = int(G_SIZE / n)

    def next_day(self):
        new_mat = self.mat.copy()
        n = self.n
        for i in range(n):
            for j in range(n):
                if self.is_alive(i, j):
                    if self.voisins[i][j] in [2, 3]:
                        pass
                    else:
                        new_mat[i, j] = 0
                else:
                    if self.voisins[i][j] == 3:
                        new_mat[i, j] = 1
        self.mat = new_mat.copy()
        self.update_neighbours()

    def update_neighbours(self):
        for i in range(self.n):
            for j in range(self.n):
                self.voisins[i][j] = self.nb_neighours(i, j)

    def is_alive(self, i, j):
        return self.mat[i, j] == 1

    def nb_neighours(self, i, j):
        ns = neighbours(i, j, self.n)
        return sum(self.mat[n] for n in ns)

    def draw(self, win):
        n = self.n
        for i in range(n):
            for j in range(n):
                color = CUTE2
                if self.is_alive(i, j):
                    color = dicolor[self.voisins[i][j]]
                left = j * self.CASE_SIZE + LEFT
                top = i * self.CASE_SIZE + TOP
                pygame.draw.rect(win, color,
                                 [left + self.CASE_SIZE * 0.05, top + self.CASE_SIZE * 0.05, self.CASE_SIZE * 0.9,
                                  self.CASE_SIZE * 0.9])

    def clear(self):
        for i in range(self.n):
            for j in range(self.n):
                self.mat[i][j] = 0
        self.update_neighbours()

    def get_pattern(self):
        res = []
        for i in range(self.n):
            for j in range(self.n):
                if self.mat[i][j] == 1:
                    res.append((i, j))
        return res

    def __repr__(self):
        s = ""
        for e in self.mat:
            s += str(e) + "\n"
        return s


dicolor = {0: CUTERED, 1: CUTERED, 2: CUTEBLUE, 3: CUTEBLUE, 4: CUTERED, 5: CUTERED, 6: CUTERED, 7: CUTERED, 8: CUTERED,
           9: CUTERED}
