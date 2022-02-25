# https://www.codewars.com/kata/connect-4/train/python
# My solution
class Connect4():
    def __init__(self):
        self.grid = [["0" for i in range(7)] for i in range(6)] # Records string to use the join function
        self.h_cols = [0 for i in range(7)]    # Record of columns pieces
        self.finished = False                  # Flag of finished game
        self.player = 1
    
    def test_connection(self, col):
        x, y, win_move = self.h_cols[col], col, str(self.player) * 4
        if "".join(self.grid[x]).find(win_move) >= 0:
            return True    # Check line
        if "".join([line[y] for line in self.grid]).find(win_move) >= 0:
            return True    # Check collumn
        
        # Sorry, but I only copy the follow code from -> https://stackoverflow.com/questions/23069388/listing-elements-in-a-nested-lists-diagonally/23069625#23069625
        # This gave me a headache 
        h, w = len(self.grid), len(self.grid[0])
        for p in range(h + w - 1):    # Check diagonals
            if "".join(self.grid[p - q][q] for q in range(max(p-h+1,0), min(p+1, w))).find(win_move) >= 0:
                return True
            if "".join(self.grid[h - p + q - 1][q] for q in range(max(p-h+1,0), min(p+1, w))).find(win_move) >= 0:
                return True
        return False
    
    def play(self, col):
        if self.finished:
            return "Game has finished!"
        if self.h_cols[col] == 6:
            return "Column full!"
            
        self.grid[self.h_cols[col]][col] = str(self.player) # Make move
        
        if self.test_connection(col):
            self.finished = True
            return "Player %d wins!" % self.player
        
        player = self.player                        # Record player
        self.player = 1 if self.player == 2 else 2  # Swap player
        self.h_cols[col] += 1                       # Update record of cols
        
        return "Player %d has a turn" % player

# ...
import re
from itertools import cycle

class Connect4():
    _WIDTH = 7
    _HEIGHT = 6
    _WIN_CONDITIONS = [re.compile(pattern) for pattern in map(r'([12])(.{{{}}}\1){{3}}'.format, (0, 5, 6, 7))]

    def __init__(self):
        self.board = ['' for __ in range(Connect4._WIDTH)]
        self.players = cycle('12')
        self.done = False
        
    def winner(self):
        board_state = '_'.join(row.ljust(Connect4._HEIGHT) for row in self.board)
        return any(pattern.search(board_state) for pattern in Connect4._WIN_CONDITIONS)
        
    def play(self, col):
        if self.done:
            return 'Game has finished!'
        if len(self.board[col]) == Connect4._HEIGHT:
            return 'Column full!'
        current_player = next(self.players)
        self.board[col] += current_player
        if self.winner():
            self.done = True
            return 'Player {} wins!'.format(current_player)
        return 'Player {} has a turn'.format(current_player)

# ...
import re

class Connect4:

    COLUMNS = 7
    ROWS = 6

    def __init__(self):
        self._board = [[0] * Connect4.COLUMNS for row in range(Connect4.ROWS)]
        self._player = 1
        self._done = False
        self._height = [0] * Connect4.COLUMNS

    def __repr__(self):
        flat_list = [str(item) for sublist in self._board for item in sublist]
        return "".join("-" + str(e) if i % 7 == 0 and i != 0 else str(e) for i, e in enumerate(flat_list))

    def drop_into_column(self, column):
        if self._height[column] == 6:
            return False
        else:
            self._board[self._height[column]][column] = self._player
            self._height[column] += 1
            return True

    def check_win_condition(self):
        board = self.__repr__()
        return re.search(r'([12])(?:\1{3}|(?:.{6}\1){3}|(?:.{7}\1){3}|(?:.{8}\1){3})', board)

    def play(self, column):
        if self._done:
            return "Game has finished!"
        if not self.drop_into_column(column):
            return "Column full!"
        else:
            if self.check_win_condition():
                self._done = True
                return "Player %d wins!" % self._player
            else:
                turn_message = "Player %d has a turn" % self._player
                if self._player == 1:
                    self._player = 2
                else:
                    self._player = 1
                return turn_message