import itertools

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


class GameOfLife:
    def __init__(self, n, pat):
        self.n = n
        self.mat = matrice(n)
        for e in pat:
            self.mat[e] = 1

    def next_day(self):
        new_mat = self.mat.copy()
        n = self.n
        for i in range(n):
            for j in range(n):
                if self.is_alive(i, j):
                    if self.nb_neighours(i, j) in [2, 3]:
                        pass
                    else:
                        new_mat[i, j] = 0
                else:
                    if self.nb_neighours(i, j) == 3:
                        new_mat[i, j] = 1
        self.mat = new_mat.copy()

    def is_alive(self, i, j):
        return self.mat[i, j] == 1

    def nb_neighours(self, i, j):
        ns = neighbours(i, j, self.n)
        return sum(self.mat[n] for n in ns)

    def draw(self, win):
        n = self.n
        CASE_SIZE = G_SIZE / n
        for i in range(n):
            for j in range(n):
                color = RED
                if self.is_alive(i, j):
                    color = WHITE
                left = j * CASE_SIZE + LEFT
                top = i * CASE_SIZE + TOP
                pygame.draw.rect(win, color, [left, top, CASE_SIZE, CASE_SIZE])

    def __repr__(self):
        s = ""
        for e in self.mat:
            s += str(e) + "\n"
        return s


m = GameOfLife(5, [(1, 2), (2, 2), (3, 2)])
