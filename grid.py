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
        self.game_over = False

    def draw_grid(self, display):
        for row in range(self.row):
            for column in range(self.cols):
                self.rect = pygame.Rect(
                    column*self.block_size, row*self.block_size, self.block_size, self.block_size)
                if self.grid[row][column] == 0:
                    pygame.draw.rect(display, (255, 255, 255), self.rect, 1)
                if self.grid[row][column] == 1:
                    pygame.draw.rect(display, (255, 0, 0), self.rect)
                if self.grid[row][column] == 2:
                    pygame.draw.rect(display, (0, 255, 0), self.rect)
                    # self.coin = pygame.image.load(
                    #     path.join(self.path, 'coin.png'))
                    # display.blit(self.coin, self.rect.center)

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
