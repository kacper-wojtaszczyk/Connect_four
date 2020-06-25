import pygame
import pygame.freetype
import sys
from board import Grid
from agent import Agent
from gui import Button, TextWindow


class Game():
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode((700, 700))
        pygame.display.set_caption("Connect four")
        self.running = True
        # self.clock = pygame.time.Clock()

    def new_game(self):
        while self.running:
            self.grid = Grid(6, 7, self)
            self.agent = Agent(self.grid, self)
            self.run()
            if self.restart():
                self.running = True
            else:
                self.running = False
            # self.reset = input("Restart (y/n) ? :\n")
            # if self.reset == "n":
            #     self.running = False

    def run(self):
        self.turn = "AGENT"
        self.playing = True
        while self.playing:
            self.check_filled()
            # self.clock.tick(30)
            self.events()
            pygame.time.wait(50)
            self.update()
            self.draw()
            if self.winning(self.grid.grid, 1) or self.winning(self.grid.grid, 2):
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

        self.keys = pygame.key.get_pressed()
        self.mouse_pos = pygame.mouse.get_pos()

        if self.keys[pygame.K_ESCAPE]:
            self.playing = False
            self.running = False
            pygame.quit()
            sys.exit()

    def update(self):
        if self.turn == "AGENT":
            self.grid.update(2)
            self.turn = "PLAYER"
            pygame.time.wait(100)
        elif self.turn == "PLAYER":
            if self.click:
                self.grid.update(1)
                pygame.time.wait(100)
                self.turn = "AGENT"
                self.click = False

        # elif self.turn == "AGENT":
        #     self.grid.update(2)
        #     self.turn = "PLAYER"

    def draw(self):
        self.game_display.fill((77, 86, 94))
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
        self.button1 = Button(
            700//2 - 140//2, 500, 140, 100, (255, 255, 255), (200, 200, 255), "START!", 40)
        self.text_window = TextWindow(50, 100, 600, 200,
                                      (255, 0, 255), "Connect four game", 80)
        self.player_choose = False
        while not self.player_choose:
            self.events()
            if self.click:
                if self.mouse_pos[0] in range(350, 490) and self.mouse_pos[1] in range(500, 600):
                    self.player_choose = True
                # self.click = False
            self.game_display.fill((0, 0, 0))
            self.button1.draw(self.game_display)
            self.text_window.draw(self.game_display)
            pygame.display.update()

    def restart(self):
        while True:
            self.text_window = TextWindow(
                50, 10, 600, 50, (255, 255, 255), "Restart?", 40)
            self.button1 = Button(
                200, 70, 100, 30, (255, 255, 255), (35, 35, 35), "YES", 20)
            self.button2 = Button(
                540, 70, 100, 30, (255, 255, 255), (35, 35, 35), "NO", 20)
            self.events()
            if self.click:
                if self.mouse_pos[0] in range(200, 300) and self.mouse_pos[1] in range(70, 100):
                    return True
                elif self.mouse_pos[0] in range(540, 640) and self.mouse_pos[1] in range(70, 100):
                    return False
            self.text_window.draw(self.game_display)
            self.button1.draw(self.game_display)
            self.button2.draw(self.game_display)
            pygame.display.flip()

    def game_over(self):
        pass


game = Game()
game.start_screen()
while game.running:
    game.new_game()
    game.game_over()

pygame.quit()
