# https://www.codewars.com/kata/escape-the-maze/train/python
# My solution
def first_position(maze):
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] in "><^v":
                return (i, j)

def walking(maze, passed, path, x, y, move):
    lin, col = len(maze), len(maze[0])
    if x < 0 or x >= lin or y < 0 or y >= col:
        return True
    if maze[x][y] == '#' or passed[x][y]:
        return False
    passed[x][y] = True
    
    if move == '>':
        r = walking(maze, passed, path, x+1, y, 'v')
        l = walking(maze, passed, path, x-1, y, '^')
        b = walking(maze, passed, path, x, y-1, '<')
        f = walking(maze, passed, path, x, y+1, '>')
    elif move == '<':
        r = walking(maze, passed, path, x-1, y, '^')
        l = walking(maze, passed, path, x+1, y, 'v')
        b = walking(maze, passed, path, x, y+1, '>')
        f = walking(maze, passed, path, x, y-1, '<')
    elif move == '^':
        r = walking(maze, passed, path, x, y+1, '>')
        l = walking(maze, passed, path, x, y-1, '<')
        b = walking(maze, passed, path, x+1, y, 'v')
        f = walking(maze, passed, path, x-1, y, '^')
    elif move == 'v':
        r = walking(maze, passed, path, x, y-1, '<')
        l = walking(maze, passed, path, x, y+1, '>')
        b = walking(maze, passed, path, x-1, y, '^')
        f = walking(maze, passed, path, x+1, y, 'v')
    
    if f:
        path += ["F"]
    elif b:
        path += ["F", "B"]
    elif r:
        path += ["F", "R"]
    elif l:
        path += ["F", "L"]
    
    return f or b or r or l

def escape(maze):
    path = []
    passed = [[False for j in range(len(maze[0]))] for i in range(len(maze))]
    i, j = first_position(maze)
    walking(maze, passed, path, i, j, maze[i][j])
    return path[::-1]

# And
def first_position(maze):
    return next((i,j) for i in range(len(maze)) for j in range(len(maze[0])) if maze[i][j] in "><^v")

# ... The rest code

# ...
def escape(maze):
    h, w = len(maze), len(maze[0])
    maze = [list(row) for row in maze]
    i, j, face = find_self(maze)
    maze[i][j] = '#'
    paths = [[i, j, face, []]]
    while paths:
        i, j, face, path = paths.pop(0)
        if i == 0 or i+1 == h or j == 0 or j+1 == w:
            return path
        for step, mi, mj, new_face in directions(i, j, face):
            if maze[mi][mj] != '#':
                paths.append([mi, mj, new_face, path+step])
                maze[mi][mj] = '#'
    return []


def find_self(maze):
    faces = {'^': (-1, 0), '<': (0, -1), 'v': (1, 0), '>': (0, 1)}
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell in faces-:
                return i, j, faces[cell]


def directions(i, j, face):
    fi, fj = face
    return [[['F'],      i+fi, j+fj, face], 
            [['L', 'F'], i-fj, j+fi, (-fj, fi)],
            [['R', 'F'], i+fj, j-fi, (fj, -fi)],
            [['B', 'F'], i-fi, j-fj, (-fi, -fj)]]