# https://www.codewars.com/kata/battleship-field-validator/train/python
# My solution
import re

def validate_battlefield(field):
    def check(field):
        for key, ship in ships.items():
            for i in range(len(field)):
                res = ship["regex"].match(field, i)
                ship["count"] = ship.get("count", 0) + (1 if res else 0)
            if ship["count"] // ship["factor"] != ship["amount"]:
                return False
        return True
    def joinx(field):
        string = "0" * 11 + ","
        string += ",".join("".join(map(str, line)) for line in field)
        string += "," + "0" * 11
        return string
    
    ships = {
        "battleship" : { "amount": 1, "factor": 1,
            "regex": re.compile("[^1]{6}.{5}[^1]1111[^1].{5}[^1]{6}")
        },
        "cruisers"   : { "amount": 2, "factor": 1,
            "regex": re.compile("[^1]{5}.{6}[^1]111[^1].{6}")
        },
        "destroyers" : { "amount": 3, "factor": 1,
            "regex": re.compile("[^1]{4}.{7}[^1]11[^1].{7}[^1]{4}")
        },
        "submarines" : { "amount": 4, "factor": 2,
            "regex": re.compile("[^1]{3}.{8}[^1]1[^1].{8}[^1]{3}")
        },
    }

    return check(joinx(field) + joinx(zip(*field)))

# Modified
from scipy.ndimage.measurements import label, find_objects, np
from collections import Counter

def validate_battlefield(field):
    field = np.array(field)
    ones = np.ones((3,3))
    labels = label(field, ones)[0]
    objects = find_objects(labels)
    ships = (field[slicer] for slicer in objects)
    return Counter(ship.size for ship in ships) == {1:4, 2:3, 3:2, 4:1}

# ...
def validateBattlefield(field):
    n, m = len(field), len(field[0])
    def cell(i, j):
        if i < 0 or j < 0 or i >= n or j >= m: return 0
        return field[i][j]
    def find(i, j):
        if cell(i + 1, j - 1) or cell(i + 1, j + 1): return 10086
        if cell(i, j + 1) and cell(i + 1, j): return 10086
        field[i][j] = 2
        if cell(i, j + 1): return find(i, j + 1) + 1
        if cell(i + 1, j): return find(i + 1, j) + 1
        return 1
    num = [0] * 5
    for i in xrange(n):
        for j in xrange(m):
            if cell(i, j) == 1:
                r = find(i, j)
                if r > 4: return False
                num[r] += 1
    [tmp, submarines, destroyers, cruisers, battleship] = num
    return battleship == 1 and cruisers == 2 and destroyers == 3 and submarines == 4

# ...
def check_outer_perimeter(field, i_offset, j_offset,
                          ship_direction, checked_cells):
    '''Checks wrapper block around the ship excluding the ship'''
    # left and right perimeter sides
    for i in xrange(i_offset - 1, i_offset + ship_direction[0] + 1):
        if 0 <= i < 10:
            j = j_offset - 1
            if j >= 0 and not checked_cells[i*10 + j] and field[i][j]:
                return False
            j = j_offset + ship_direction[1]
            if j < 10 and not checked_cells[i*10 + j] and field[i][j]:
                return False

    # down perimeter side
    for j in xrange(j_offset, j_offset + ship_direction[1]):
        if i < 10:
            i = i_offset + ship_direction[0]
            if field[i][j]:
                return False

    return True


def get_direction(field, i_offset, j_offset):
    '''Gets length of the ship in X and Y axis:
        "i" is how long to down
        "j" is how long to right
    '''
    i = j = 0
    while i_offset + i < 10 and field[i_offset+i][j_offset]:
        i += 1
    while j_offset + j < 10 and field[i_offset][j_offset+j]:
        j += 1
    return i, j


def validate_battlefield(field):
    '''Directly checks if the field is correct'''
    ships_rest = {1: 4,
                  2: 3,
                  3: 2,
                  4: 1}
    checked_cells = [False for _ in xrange(10*10)]

    if sum(sum(cell for cell in row) for row in field) != 20:
        return False

    for i in xrange(len(field)):
        for j in xrange(len(field)):
            if not checked_cells[i*10 + j] and field[i][j]:
                ship_dir = get_direction(field, i, j)
                ship_len = max(ship_dir)

                if ship_len not in ships_rest or ships_rest[ship_len] == 0:
                    return False  # len is 5+ or wrong ships set
                if sum(ship_dir) != ship_len + 1:
                    return False  # linear ships
                if not check_outer_perimeter(field, i, j, ship_dir, checked_cells):
                    return False  # some ships are too close to each other

                for x in xrange(j, j + ship_dir[1]):
                    checked_cells[i*10 + x] = True
                for y in xrange(i, i + ship_dir[0]):
                    checked_cells[y*10 + j] = True

                ships_rest[ship_len] -= 1
            else:
                checked_cells[i*10 + j] = True

    return True
    
validateBattlefield = lambda x: validate_battlefield(x)

# ...
# Combines the advantages of generators and quick exit when you find something that clearly isn't good.

# check that the total sum is correct
# use a flood-fill algo as a generator on a copy of the field array, that generator yielding the sizes of the boats
# the while loop with the divmod moves the "pointer" in the field like two nested loops would do it => goes to the next 1 in the grid
# stops the generator if went out of the field
# otherwise, flood-fill an area of 1 and adjacent ones, erasing them in field
# then checks that all the found coordinates are on a uniq line (first term of valid)...
# yield valid (the size of that boat then go deeper in the search, or False if invalid situation)
# if not valid, the boolean yielded will make fail the Counter comparison and the generator is stoped at this point in the recursion.
# from collections import Counter

MOVES = ((0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (-1,1), (1,-1))
VALID = {4:1, 3:2, 2:3, 1:4}

def validateBattlefield(field):
    return sum(map(sum,field))==20 and Counter(flood(list(map(list,field))))==VALID
    
def flood(field, x=0, y=0):
    while x<10 and not field[x][y]: x,y = divmod(10*x+y+1,10)
    if x<10:
        bag, found = {(x,y)}, set()
        while bag:
            found |= bag
            for a,b in bag: field[a][b]=0
            bag = {(a+dx,b+dy) for a,b in bag for dx,dy in MOVES if 0<=a+dx<10 and 0<=b+dy<10 and field[a+dx][b+dy]}
        valid = 1 in {len(set(dim)) for dim in zip(*found)} and len(found)
        yield valid
        if valid: yield from flood(field,x,y)

# ...
from scipy.ndimage.measurements import label, find_objects, np
def validate_battlefield(field):
    field = np.array(field)
    return sorted(
        ship.size if min(ship.shape) == 1 else 0
        for ship in (field[pos] for pos in find_objects(label(field, np.ones((3,3)))[0]))
    ) == [1,1,1,1,2,2,2,3,3,4]

# ...
def validateBattlefield(field):  
    ships = []
    
    #this algorithm uses the field 2-dimensional array it self to store infomration about the size of ships found      
    for i in range(0, 10):            
        for j in range(0, 10):  
            #if not at end of any edge in 2d-array, check that sum of two cross diagonal elements is not more than max 
            #if it is then two ships are two close
            if j < 9 and i < 9: 
                if field[i][j] + field[i+1][j+1] > max(field[i][j], field[i+1][j+1]): 
                    return False 
                if field[i+1][j] + field[i][j+1] > max(field[i+1][j], field[i][j+1]):
                    return False
            #if the element at position (i, j) is occupied then add the current value of position to next
            if j < 9 and field[i][j] > 0 and field[i][j+1] > 0:
                field[i][j+1] += field[i][j]
            elif i < 9 and field[i][j] > 0 and field[i+1][j] > 0:
                field[i+1][j] += field[i][j]
            elif field[i][j] > 0:
                ships.append(field[i][j]) #since we add numbers
                
    ships.sort()

    return ships == [1, 1, 1, 1, 2, 2, 2, 3, 3, 4] #if the ships we have found are of correct configuration then it will equal this array

# ...
from scipy.signal import convolve2d as conv
def validateBattlefield(f):
    b = [[[[1 for j in range(i)]],[[1] for j in range(i)]] for i in range(1,5)]
    b += [[[[1,0],[0,1]],[[0,1],[1,0]]]]
    count = [1,2,3,4,2]
    c = [40,10,4,1,0]
    for i in range(5):
        c0 = conv(f,b[i][0])
        c1 = conv(f,b[i][1])
        if sum([list(j).count(count[i]) for j in c0]) + sum([list(j).count(count[i]) for j in c1]) != c[i]:
            return False
    return True

# ...
from itertools import chain
from collections import Counter

def validateBattlefield(b):
    row = [''.join([str(i) for i in ele]).replace('0',' ').split() for ele in b]
    column = [''.join([str(i) for i in ele]).replace('0',' ').split() for ele in list(zip(*b))]
    cnt = Counter(chain.from_iterable(row)) + Counter(chain.from_iterable(column))
    if cnt['1'] == 24 and cnt['11'] == 3 and cnt['111'] == 2 and cnt['1111'] == 1:
        # check if ships are in contact by their corner
        for i in range(1,10):
            for j in range(1,10):
                if b[i][j] == 1:
                    if b[i-1][j-1] == 1 or b[i+1][j-1] == 1 or b[i-1][j+1] == 1 or b[i+1][j+1] == 1:
                        return False
        return True
    return False