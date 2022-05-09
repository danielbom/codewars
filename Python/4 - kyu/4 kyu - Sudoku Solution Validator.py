# https://www.codewars.com/kata/529bf0e9bdf7657179000008/train/python
# My solution
def valid_solution(board):
    for row in board:
        for col in row:
            if col == 0:
                return False

    for row in board:
        if len(set(row)) != 9:
            return False

    cols = [set() for i in range(9)]
    for row in board:
        for i, col in enumerate(row):
            cols[i].add(col)
    for i, c in enumerate(cols):
        if len(c) != 9:
            return False
    
    quads, iquads = [], 0
    for i in range(0, 3):
        for j in range(0, 3):
            x = i * 3
            y = j * 3
            quads.append(set())
            for xx in range(0, 3):
                for yy in range(0, 3):
                    quads[iquads].add(board[x + xx][y + yy])
            iquads += 1
    for q in quads:
        if len(q) != 9:
            return False

    return True

# And
def valid_solution(board):
    if any(col == 0 for row in board for col in row):
        return False

    if any(sum(row) != 45 for row in board):
        return False
    
    if any(sum(board[j][i] for j in range(9)) != 45 for i in range(9)):
        return False
    
    range33 = lambda : ((i, j) for j in range(0, 3) for i in range(0, 3))
    if any(sum(board[i * 3 + xx][j * 3 + yy] for xx, yy in range33()) != 45 for i, j in range33()):
        return False

    return True

# ...
def validSolution(board):
    blocks = [[board[x+a][y+b] for a in (0, 1, 2) for b in (0, 1, 2)] for x in (0, 3, 6) for y in (0, 3, 6)]
    return not filter(lambda x: set(x) != set(range(1, 10)), board + zip(*board) + blocks)

# Modified
from itertools import chain
def valid_solution(board):
    blocks = ((board[x+a][y+b] for a in (0, 1, 2) for b in (0, 1, 2)) for x in (0, 3, 6) for y in (0, 3, 6))
    return all(sum(set(x)) == 45 for x in chain(board, zip(*board), blocks))

# ...
import numpy as np
from itertools import chain

nums = set(range(1, 10))

def validSolution(board):
    a = np.array(board)
    r = range(0, 9, 3)
    return all(set(v.flatten()) == nums for v in chain(a, a.T, (a[i:i+3, j:j+3] for i in r for j in r)))

# ...
def validSolution(board):
    for x in range(9):
        arr = [board[y][x] for y in range(9)]
        arr2 = [board[x][y] for y in range(9)]
        arr3 = [board[i][y] for y in range(((x%3)*3),(((x%3)*3)+3)) for i in range((int(x/3)*3),(int(x/3)*3)+3)]
        for i in range(9):
            if arr[i] in arr[(i+1):]: return False
            if arr2[i] in arr2[(i+1):]: return False
            if arr3[i] in arr3[(i+1):]: return False
    return True