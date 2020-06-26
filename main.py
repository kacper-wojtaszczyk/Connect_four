import pygame
import sys
import config
from board import Grid
from agent import Agent
from gui import Button, TextWindow


class Game():
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode(
            (config.display_w, config.display_h))
        pygame.display.set_caption(config.caption)
        self.running = True
        self.clock = pygame.time.Clock()
        self.click = False

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
            if self.winning(self.grid.grid, config.player_mark) or self.winning(self.grid.grid, config.AI_mark):
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
        self.button1 = Button(config.button1_x, config.button1_y, config.button1_w, config.button1_h,
                              config.BLACK, config.button_color, config.button1_text, config.button1_fontsize)
        self.text_window = TextWindow(config.text1_x, config.text1_y, config.text1_w, config.text1_h,
                                      config.board_color, config.text1_text, config.text1_fontsize)
        self.player_choose = False
        while not self.player_choose:
            self.events()
            if self.mouse_pos[0] in range(config.button1_x, config.button1_x + config.button1_w) and self.mouse_pos[1] in range(config.button1_y, config.button1_y + config.button1_h):
                self.button1.background_color = config.button_effect_color
                if self.click:
                    self.player_choose = True
            else:
                self.button1.background_color = config.button_color
            self.game_display.fill(config.bg_color)
            self.button1.draw(self.game_display)
            self.text_window.draw(self.game_display)
            pygame.display.update()

    def restart(self):
        while True:
            self.text_window = TextWindow(config.text2_x, config.text2_y, config.text2_w,
                                          config.text2_h, config.board_color, config.text2_text, config.text2_fontsize)
            self.button2 = Button(config.button2_x, config.button2_y, config.button2_w, config.button2_h,
                                  config.BLACK, config.button_color, config.button2_text, config.button2_fontsize)
            self.button3 = Button(config.button3_x, config.button3_y, config.button3_w, config.button3_h,
                                  config.BLACK, config.button_color, config.button3_text, config.button3_fontsize)
            self.events()
            if self.mouse_pos[0] in range(config.button2_x, config.button2_x + config.button2_w) and self.mouse_pos[1] in range(config.button2_y, config.button2_y + config.button2_h):
                self.button2.background_color = config.button_effect_color
                if self.click:
                    return True
            elif self.mouse_pos[0] in range(config.button3_x, config.button3_x + config.button3_w) and self.mouse_pos[1] in range(config.button3_y, config.button3_y + config.button3_h):
                self.button3.background_color = config.button_effect_color
                if self.click:
                    return False
            else:
                self.button2.background_color = config.button_color
                self.button3.background_color = config.button_color
            self.text_window.draw(self.game_display)
            self.button2.draw(self.game_display)
            self.button3.draw(self.game_display)
            pygame.display.flip()

    def game_over(self):
        pass


game = Game()
game.start_screen()
while game.running:
    game.new_game()
    game.game_over()

pygame.quit()
