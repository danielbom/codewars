# https://www.codewars.com/kata/connect-four-1/train/python
# My solution
import string


def test(table):
    def go_right(table, x, y, count, player):
        if count == 4:
            return True
        if y < 7 and table[x][y] == player:
            return go_right(table, x, y+1, count+1, player)
        return False
    
    def go_down(table, x, y, count, player):
        if count == 4:
            return True
        if x < 6 and table[x][y] == player:
            return go_down(table, x+1, y, count+1, player)
        return False
    
    def go_diag1(table, x, y, count, player):
        if count == 4:
            return True
        if x < 6 and y < 7 and table[x][y] == player:
            return go_diag1(table, x+1, y+1, count+1, player)
        return False
    
    def go_diag2(table, x, y, count, player):
        if count == 4:
            return True
        if x >= 0 and y < 7 and table[x][y] == player:
            return go_diag2(table, x-1, y+1, count+1, player)
        return False
        
    for i in range(4):
        for j in range(7):
            if table[i][j] != 0 and (
                    go_right(table, i, j, 0, table[i][j]) or
                    go_down(table, i, j, 0, table[i][j]) or
                    go_diag1(table, i, j, 0, table[i][j]) or
                    go_diag2(table, i, j, 0, table[i][j])
            ):
                return True
def who_is_winner(pieces_position_list):
    players = {"Y" : 1, "R" : 2}
    
    table = [[0 for i in range(7)] for j in range(6)]
    height = [0 for i in range(7)]
    
    for p in pieces_position_list:
        # Posição da peça
        y = string.ascii_uppercase.index( p[0] )
        x = height[y]
        height[y] += 1
        
        table[x][y] = players[p[2]] # Inserindo a peça do jogador
        
        if test(table):
            return "Yellow" if table[x][y] == 1 else "Red"
    return "Draw"

# ...
import numpy as np
from scipy.signal import convolve2d
def who_is_winner(pieces_position_list):
    arr = np.zeros((7,6), int)
    for a in pieces_position_list:
        pos, color = a.split('_')
        pos = ord(pos) - ord('A')
        val = (-1,1)[color == 'Red']
        arr[pos, np.argmin(arr[pos] != 0)] = val
        t_arr = val * arr
        if any(np.max(cv) == 4 for cv in (convolve2d(t_arr, [[1,1,1,1]], 'same'),
                                          convolve2d(t_arr, [[1],[1],[1],[1]], 'same'),
                                          convolve2d(t_arr, [[1,0,0,0], [0,1,0,0], [0,0,1,0], [0,0,0,1]], 'same'),
                                          convolve2d(t_arr, [[0,0,0,1], [0,0,1,0], [0,1,0,0], [1,0,0,0]], 'same'))):
            return color
    return 'Draw'

# ...
import numpy as np
def who_is_winner(pieces_position_list):
    ROW_COUNT = 6
    COLUMN_COUNT = 7
    YELLOW = 1
    RED = 2
    my_dict = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6
    }
    moves = [n.split("_") for n in pieces_position_list]

    def create_board():
        board = np.zeros((ROW_COUNT, COLUMN_COUNT))
        return board

    def drop_piece(board, row, column, piece):
        board[row][column] = piece

    def is_valid_location(board, column):
        if column in range(COLUMN_COUNT):
            return True
        else:
            return False

    def get_next_open_row():
        for r in range(ROW_COUNT):
            if board[r][column] == 0:
                return r


    def winnning_move(board, piece):
        # check horizontal locations
        for r in range(ROW_COUNT):
            for c in range(COLUMN_COUNT - 3):
                if board[r][c] == piece and board[r][c + 1] == piece \
                        and board[r][c + 2] == piece and board[r][c + 3] == piece:
                    return True

        # check vertical locations
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if board[r][c] == piece and board[r + 1][c] == piece \
                        and board[r + 2][c] == piece and board[r + 3][c] == piece:
                    return True

        # check positive sloped diagonal "/" - diagonal"
        for r in range(ROW_COUNT - 3):
            for c in range(COLUMN_COUNT - 3):
                if board[r][c] == piece and board[r + 1][c + 1] == piece \
                        and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                    return True

        # check negative sloped diagonal "\" - diagonal"
        for r in range(3, ROW_COUNT):
            for c in range(COLUMN_COUNT - 3):
                if board[r][c] == piece and board[r - 1][c + 1] == piece \
                        and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                    return True

    board = create_board()

    while moves:
        column = moves.pop(0)
        column_piece = column[1]
        if column_piece == "Red":
            # choose your column
            column = my_dict[column[0]]
            if is_valid_location(board, column):
                row = get_next_open_row()
                drop_piece(board, row, column, RED)

                if winnning_move(board, RED):
                    return "Red"
        else:
            # choose your column
            column = my_dict[column[0]]
            if is_valid_location(board, column):
                row = get_next_open_row()
                drop_piece(board, row, column, YELLOW)

                if winnning_move(board, YELLOW):
                    return "Yellow"

    return "Draw"