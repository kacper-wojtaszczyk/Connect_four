import pygame
import sys
import config
import gui
from board import Grid
from agent import Agent


class Game():
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode(
            (config.display_w, config.display_h))
        pygame.display.set_caption(config.caption)
        self.running = True
        self.clock = pygame.time.Clock()
        self.click = False
        self.player_win = False
        self.difficulty = False
        self.choose = None

    def new_game(self):
        while self.running:
            self.grid = Grid(config.rows, config.columns, self)
            self.agent = Agent(self.grid, self)
            self.run()
            if self.restart():
                self.running = True
            else:
                self.running = False

    def run(self):
        self.turn = config.AI_turn
        self.playing = True
        while self.playing:
            self.check_filled()
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()
            if self.winning(self.grid.grid, config.player_mark):
                self.player_win = True
                self.playing = False
            elif self.winning(self.grid.grid, config.AI_mark):
                self.playing = False

    def events(self):
        self.click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.click = True

        self.mouse_pos = pygame.mouse.get_pos()
        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_ESCAPE]:
            self.playing = False
            self.running = False
            pygame.quit()
            sys.exit()

    def update(self):
        if self.turn == config.AI_turn:
            self.grid.update(config.AI_mark)
            self.turn += 1
            self.turn = self.turn % 2
        elif self.turn == config.player_turn:
            if self.click:
                self.grid.update(config.player_mark)
                self.turn += 1
                self.turn = self.turn % 2

    def draw(self):
        self.game_display.fill(config.bg_color)
        self.grid.draw_grid(self.game_display)
        pygame.display.update()

    def check_filled(self):
        self.filled_spots = 0
        for columns in range(self.grid.cols):
            if self.grid.open_spot(columns) == "XD":
                self.filled_spots += 1

        if self.filled_spots == self.grid.cols:
            self.playing = False

    def winning(self, grid, piece):

        # Horizontal
        for row in range(self.grid.row):
            for column in range(self.grid.cols - (config.inarow - 1)):
                self.window = list(grid[row, column:column+config.inarow])
                if self.window.count(piece) == config.inarow:
                    return True

        # Vertical
        for row in range(self.grid.row - (config.inarow - 1)):
            for column in range(self.grid.cols):
                self.window = list(grid[row:row+config.inarow, column])
                if self.window.count(piece) == config.inarow:
                    return True

        # Positive diagonal
        for row in range(self.grid.row - (config.inarow - 1)):
            for column in range(self.grid.cols - (config.inarow - 1)):
                self.window = list(grid[range(
                    row, row+config.inarow), range(column, column+config.inarow)])
                if self.window.count(piece) == config.inarow:
                    return True

        # Negative diagonal
        for row in range((config.inarow - 1), self.grid.row):
            for column in range(self.grid.cols - (config.inarow - 1)):
                self.window = list(grid[range(
                    row, row-config.inarow, -1), range(column, column + config.inarow)])
                if self.window.count(piece) == config.inarow:
                    return True

        return False

    def start_screen(self):
        self.start = False
        while not self.start:
            self.events()
            self.start = gui.start_screen(
                self.mouse_pos, self.click, self.game_display)

    def restart(self):
        self.reset = False
        if self.player_win:
            self.winner = config.player_mark
        else:
            self.winner = config.AI_mark
        while not self.reset:
            self.events()
            self.choose = gui.restart_screen(
                self.mouse_pos, self.click, self.game_display, self.winner)
            if self.choose:
                return self.choose
            elif self.choose == False:
                return self.choose
            else:
                pass

    def game_over(self):
        pass

    def difficulty_screen(self):
        while not self.difficulty:
            self.events()
            self. difficulty = gui.difficulty_screen(
                self.mouse_pos, self.click, self.game_display)


game = Game()
game.start_screen()
game.difficulty_screen()
while game.running:
    game.new_game()
    game.game_over()

pygame.quit()
