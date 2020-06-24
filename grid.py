import numpy as np
import pygame
import math
from os import path


class Grid():
    def __init__(self, row, cols, game):
        self.row = row
        self.cols = cols
        self.grid = np.zeros((self.row, self.cols), dtype=int)
        self.game = game
        self.path = path.dirname(__file__)
        self.block_size = 100
        self.circle_radius = 40
        self.game_over = False

    def draw_grid(self, display):
        for row in range(self.row):
            for column in range(self.cols):
                self.rect = pygame.Rect(
                    column*self.block_size, (row + 1)*self.block_size,  self.block_size, self.block_size)

                pygame.draw.rect(display, (95, 164, 237), self.rect)
                pygame.draw.rect(display, (0, 0, 0), self.rect, 1)
                pygame.draw.circle(display, (77, 86, 94),
                                   self.rect.center, self.circle_radius)
                pygame.draw.circle(display, (0, 0, 0),
                                   self.rect.center, self.circle_radius, 1)
                if self.grid[row][column] == 1:
                    pygame.draw.circle(display, (20, 200, 13),
                                       (self.rect.center), self.circle_radius)
                if self.grid[row][column] == 2:
                    pygame.draw.circle(display, (186, 45, 10),
                                       (self.rect.center), self.circle_radius)

    def open_spot(self, check_col):
        for x in range(self.row - 1, -1, -1):
            if self.grid[x][check_col] == 0:
                return x
        return "XD"

    def get_column(self):
        self.pos_x = self.game.mouse_pos[0]
        return int(math.floor(self.pos_x/self.block_size))

    def update(self, mark):
        if self.game_over == False:
            if mark == 1:
                self.update_column = self.get_column()
                self.update_row = self.open_spot(self.update_column)
                if self.update_row != "XD":
                    self.grid[self.update_row][self.update_column] = mark
                elif self.update_row == "XD":
                    return False
            elif mark == 2:
                self.update_column = self.game.agent.next_move()
                self.update_row = self.open_spot(self.update_column)
                self.grid[self.update_row][self.update_column] = mark
        else:
            return False
