import random
import config
import numpy as np


class Agent():
    def __init__(self, grid, game):
        self.mark = config.AI_mark
        self.grid = grid
        self.game = game
        self.n_steps = config.minimax_steps

    def valid_moves(self, grid):
        self.valid_moves_list = []
        for column in range(self.grid.cols):
            for row in range(self.grid.row - 1, -1, -1):
                if grid[row][column] == 0:
                    if column not in self.valid_moves_list:
                        self.valid_moves_list.append(column)
        return self.valid_moves_list

    def next_drop(self, grid, column, piece):
        next_grid = grid.copy()
        for row in range(self.grid.row - 1, -1, -1):
            if next_grid[row][column] == 0:
                break
        next_grid[row][column] = piece
        return next_grid

    def check_winning_move(self, column_to_check, piece):
        self.next = self.next_drop(self.grid.grid, column_to_check, piece)
        return self.game.winning(self.next, piece)

    def score_move(self, column_to_check, piece):
        self.next = self.next_drop(self.grid.grid, column_to_check, piece)
        return self.minimax(self.next, self.n_steps - 1, False, piece)

    def is_terminal_window(self, window):
        return window.count(config.player_mark) == config.inarow or window.count(config.AI_mark) == config.inarow

    def is_terminal_node(self, grid):
        if list(grid[0, :]).count(0) == 0:
            return True

        # Horizontal
        for row in range(self.grid.row):
            for column in range(self.grid.cols - (config.inarow - 1)):
                self.window = list(grid[row, column:column + config.inarow])
                if self.is_terminal_window(self.window):
                    return True

        # Vertical
        for row in range(self.grid.row - (config.inarow - 1)):
            for column in range(self.grid.cols):
                self.window = list(grid[row:row + config.inarow, column])
                if self.is_terminal_window(self.window):
                    return True

        # Poisitive diagonal
        for row in range(self.grid.row - (config.inarow - 1)):
            for column in range(self.grid.cols - (config.inarow - 1)):
                self.window = list(
                    grid[range(row, row + config.inarow), range(column, column + config.inarow)])
                if self.is_terminal_window(self.window):
                    return True

        # Negative diagonal
        for row in range(3, self.grid.row):
            for column in range(self.grid.cols - (config.inarow - 1)):
                self.window = list(
                    grid[range(row, row - config.inarow, -1), range(column, column + config.inarow)])
                if self.is_terminal_window(self.window):
                    return True

        return False

    def minimax(self, grid, depth, max_Player, piece):
        self.is_terminal = self.is_terminal_node(grid)
        if depth == 0 or self.is_terminal:
            return self.get_heuristic(grid, piece)
        if max_Player:
            self.value = -np.Inf
            for column in self.valid_moves(grid):
                self.child = self.next_drop(grid, column, piece - 1)
                self.value = max(self.value, self.minimax(
                    self.child, depth - 1, False, piece))
            return self.value
        else:
            self.value = np.Inf
            for column in self.valid_moves(grid):
                self.child = self.next_drop(grid, column, piece)
                self.value = min(self.value, self.minimax(
                    self.child, depth - 1, True, piece))
            return self.value

    def get_heuristic(self, grid, piece):
        #self.twos = self.count_windows(grid, 2, piece)
        self.threes = self.count_windows(grid, 3, piece)
        self.fours = self.count_windows(grid, 4, piece)
        #self.twos_opposite = self.count_windows(grid, 2, piece - 1)
        self.threes_opposite = self.count_windows(grid, 3, piece - 1)
        self.score = config.fours*self.fours + config.threes * \
            self.threes + config.threes_opp*self.threes_opposite
        return self.score

    def check_window(self, window, num_disc, piece):
        return (window.count(piece) == num_disc and window.count(0) == config.inarow - num_disc)

    def count_windows(self, grid, num_disc, piece):
        self.num_windows = 0

        # Horizontal
        for row in range(self.grid.row):
            for column in range(self.grid.cols - (config.inarow - 1)):
                self.window = list(grid[row, column:column+config.inarow])
                if self.check_window(self.window, num_disc, piece):
                    self.num_windows += 1

        # Vertical
        for row in range(self.grid.row - (config.inarow - 1)):
            for column in range(self.grid.cols):
                self.window = list(grid[row:row + config.inarow, column])
                if self.check_window(self.window, num_disc, piece):
                    self.num_windows += 1

        # Poisitive diagonal
        for row in range(self.grid.row - (config.inarow - 1)):
            for column in range(self.grid.cols - (config.inarow - 1)):
                self.window = list(
                    grid[range(row, row + config.inarow), range(column, column + config.inarow)])
                if self.check_window(self.window, num_disc, piece):
                    self.num_windows += 1

        # Negative diagonal
        for row in range(3, self.grid.row):
            for column in range(self.grid.cols - (config.inarow - 1)):
                self.window = list(
                    grid[range(row, row - config.inarow, -1), range(column, column + config.inarow)])
                if self.check_window(self.window, num_disc, piece):
                    self.num_windows += 1

        return self.num_windows

    def next_move(self):
        self.moves = self.valid_moves(self.grid.grid)
        self.scores = dict(
            zip(self.moves, [self.score_move(column, self.mark) for column in self.moves]))
        self.max_cols = [key for key in self.scores.keys(
        ) if self.scores[key] == max(self.scores.values())]

        return random.choice(self.max_cols)
        # if len(self.moves) != 0:
        #     for move in self.moves:
        #         if self.check_winning_move(move, 1):
        #             return move
        #         if self.check_winning_move(move, self.mark):
        #             return move
        #     return random.choice(self.moves)
