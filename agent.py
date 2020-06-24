import random


class Agent():
    def __init__(self, grid, game):
        self.mark = 2
        self.color = (0, 255, 0)
        self.grid = grid
        self.game = game

    def valid_moves(self):
        self.valid_moves_list = []
        for column in range(self.grid.cols):
            for row in range(self.grid.row - 1, -1, -1):
                if self.grid.grid[row][column] == 0:
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

    def next_move(self):
        self.moves = self.valid_moves()
        if len(self.moves) != 0:
            for move in self.moves:
                if self.check_winning_move(move, 1):
                    return move
                if self.check_winning_move(move, self.mark):
                    return move
            return random.choice(self.moves)
        else:
            self.grid.game_over = True
