import pygame
import pygame.freetype
import sys
# import numpy as np
# from os import path
from grid import Grid
from agent import Agent


class Game():
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode((700, 700))
        pygame.display.set_caption("Connect four")
        self.running = True
        self.clock = pygame.time.Clock()
        self.click = False

    def new_game(self):
        self.turn = "AGENT"
        self.running = True
        while self.running:
            self.grid = Grid(6, 7, self)
            self.agent = Agent(self.grid, self)
            self.run()
            print("Game over\n")
            self.reset = input("Restart (y/n) ? :\n")
            if self.reset == "n":
                self.running = False

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(30)
            self.events()
            self.update()
            self.draw()
            if self.winning(self.grid.grid, 1) or self.winning(self.grid.grid, 2):
                self.playing = False

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT and self.playing:
                self.playing = False
                self.running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and self.playing:
                self.click = True

        self.keys = pygame.key.get_pressed()
        self.mouse_pos = pygame.mouse.get_pos()

        if self.keys[pygame.K_ESCAPE] and self.playing:
            self.playing = False
            self.running = False
            pygame.quit()
            sys.exit()

    def update(self):
        if self.turn == "PLAYER":
            if self.click:
                self.grid.update(1)
                self.click = False
                self.turn = "AGENT"
                pygame.time.wait(100)
        elif self.turn == "AGENT":
            pygame.time.wait(100)
            self.grid.update(2)
            self.turn = "PLAYER"

    def draw(self):
        self.game_display.fill((77, 86, 94))
        self.grid.draw_grid(self.game_display)
        pygame.display.update()

    def winning(self, grid, piece):

        # Horizontal
        for row in range(self.grid.row):
            for column in range(self.grid.cols - 3):
                self.window = list(grid[row, column:column+4])
                if self.window.count(piece) == 4:
                    return True

        # Vertical
        for row in range(self.grid.row - 3):
            for column in range(self.grid.cols):
                self.window = list(grid[row:row+4, column])
                if self.window.count(piece) == 4:
                    return True

        # Positive diagonal
        for row in range(self.grid.row - 3):
            for column in range(self.grid.cols - 3):
                self.window = list(grid[range(
                    row, row+4), range(column, column+4)])
                if self.window.count(piece) == 4:
                    return True

        # Negative diagonal
        for row in range(3, self.grid.row):
            for column in range(self.grid.cols - 3):
                self.window = list(grid[range(
                    row, row-4, -1), range(column, column + 4)])
                if self.window.count(piece) == 4:
                    return True

        return False

    def start_screen(self):
        pass

    def game_over(self):
        pass


game = Game()
game.start_screen()
while game.running:
    game.new_game()
    game.game_over()

pygame.quit()
