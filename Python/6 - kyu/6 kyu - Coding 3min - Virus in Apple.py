# https://www.codewars.com/kata/coding-3min-virus-in-apple/train/python
# My solution
def pattern_form(n):
    pattern = "{:^%d}" % n
    for i in range(n//2):
        yield pattern.format("*" * ((i*2)+1))
    for i in range(n//2, -1, -1):
        yield pattern.format("*" * ((i*2)+1))

def infect_apple(apple, n):
    lin,col = len(apple), len(apple[0])
    result = [['A' for j in range(col)] for i in range(lin)]
    
    length = (2*n)+1
    for i in range(lin):
        for j in range(col):
            if apple[i][j] == 'V':
                xx, yy = i-(length//2), j-(length//2)
                for k, pattern in enumerate(pattern_form(length)):
                    for l, c in enumerate(pattern):
                        if c == '*' and 0 <= xx+k < lin and 0 <= yy+l < col:
                            print(xx+k, yy+l)
                            result[xx+k][yy+l] = 'V'
    return result

# ...
def infect_apple(apple, n):
    A = {(r, c):v for r, row in enumerate(apple) for c, v in enumerate(row)}

    for _ in range(n):
        for n in {(r, c) for r, c in A if any(A.get((r+rr, c+cc), '') == 'V' for rr, cc in [(1, 0), (-1, 0), (0, 1), (0,-1)])}:
            A[n] = 'V'
        
    return [[A[(r, c)] for c in range(len(apple[0]))] for r in range(len(apple))]

# ...
import numpy as np
from scipy.signal import convolve2d
def infect_apple(apple, n):
    arr = np.array([[b == 'V' for b in a] for a in apple], np.int)
    for a in range(n):
        arr = convolve2d(arr, [[0,1,0], [1,1,1], [0,1,0]], 'same')
    return [['AV'[b > 0] for b in a] for a in arr]

# ...
MOVES = ((0,1), (1,0), (0,-1), (-1,0))

def infect_apple(apple,n):
    def isVirusAround(x,y):
        return any( 0<=x+dx<len(apple) and 0<=y+dy<len(apple[0]) and apple[x+dx][y+dy]=='V'
                    for dx,dy in MOVES)
    for _ in range(n):
        apple = [['V' if c=='V' or isVirusAround(x,y) else 'A' for y,c in enumerate(r)]
                 for x,r in enumerate(apple) ]
    return apple