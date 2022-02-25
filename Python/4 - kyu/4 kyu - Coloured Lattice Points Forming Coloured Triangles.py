# https://www.codewars.com/kata/coloured-lattice-points-forming-coloured-triangles/train/python
# My solution
from collections import deque
import itertools, operator
import numpy as np

def valid_triangle(a, b, c):
    return round(np.linalg.det([[*a,1],[*b,1],[*c,1]]), 3) != 0

def count_col_triang(points):
    colors = {p[1] : deque() for p in points}
    colors_n = {p[1] : 0 for p in points}
    for p in points: colors[p[1]].append(p[0])
    
    triangles_n = 0
    for c in colors:
        for p in itertools.combinations(colors[c], 3):
            if valid_triangle(p[0],p[1],p[2]):
                colors_n[c] += 1
                triangles_n += 1
    
    most_count = max(colors_n.values())
    most = [c for c, n in colors_n.items() if n == most_count]
    most = [] if most_count == 0 else (list(sorted(most)) + [most_count])
    
    return [len(points), len(colors_n), triangles_n, most]

# ...
from itertools import combinations

def count_col_triang(a):
    p, r = {}, {}
    for xy, col in a:
        p[col] = p.get(col, []) + [xy]
    for k in p:
        r[k] = sum(1 for c in combinations(p[k], 3) if triangle(*c))
    mx = max(r.values())
    return [len(a), len(p), sum(r.values()), sorted(k for k in r if r[k] == mx) + [mx] if mx else []]
    
def triangle(a, b, c):  
    return area(*[((p[0] - q[0])**2 + (p[1] - q[1])**2)**0.5 for p, q in [(a, b), (a, c), (b, c)]]) > 0.0

def area(a, b, c):
    s = 0.5 * (a + b + c)
    return round(max((s*((s-a)*(s-b)*(s-c))), 0.0)**0.5, 4)

# ...
from itertools import combinations, groupby
def count_col_triang(input):
    is_triangle = lambda (xa, ya), (xb, yb), (xc, yc): xa * (yb - yc) + ya * (xc - xb) + xb * yc - xc * yb != 0
    colors = {color: sum(1 for tr in combinations((p for p, _ in points), 3) if is_triangle(*tr))
              for color, points in groupby(sorted(input, key=lambda v: v[1]), lambda v: v[1])}
    m = max(colors.values())
    return [len(input), len(colors), sum(colors.values()), sorted(k for k, v in colors.items() if v == m) + [m] if m > 0 else []]

# ...
from numpy.linalg import det as determinant
from itertools import permutations, combinations

def distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def is_triangle(list_of_points):
    lengths = [distance(list_of_points[p[0]], list_of_points[p[1]]) for p in permutations(range(3), 2)]
    return True if lengths[0] + lengths[1] > lengths[2] and lengths[1] + lengths[2] > lengths[0] and lengths[0] + lengths[2] > lengths[1] else False

def count_col_triang(input_):
    colours = set([element[1] for element in input_])
    dict_triangles = {}
    for colour in colours:
        dict_triangles[colour] = 0
        points = [element[0] for element in input_ if element[1] == colour]
        for combination in combinations(points, 3):
            if determinant([combination[0] + [1], combination[1] + [1], combination[2] + [1]]):
                dict_triangles[colour] += 1
    max_colour = []
    if sum(dict_triangles.values()) > 0:                
        sorted_keys = sorted(dict_triangles, key=dict_triangles.__getitem__)
        count = dict_triangles.values().count(max(dict_triangles.values()))
        for i in range(0, count):
            max_colour += [sorted_keys[-1]]
            sorted_keys = sorted_keys[:-1]
        max_colour.sort()
        max_colour += [max(dict_triangles.values())]
    return [len(input_), len(colours), sum(dict_triangles.values()), max_colour]

# ...
from itertools   import combinations
from collections import defaultdict

def crossProd(v1, v2):   return v1[0]*v2[1] - v2[0]*v1[1]
def vectorize(pt1, pt2): return [b-a for a,b in zip(pt1, pt2)]
def notOnSameLine(*pts): return bool( crossProd(vectorize(*pts[:2]), vectorize(*pts[1:])) )

def count_col_triang(input_):
    dctPts = defaultdict(list)
    for pos,color in input_: dctPts[color].append(pos)
    
    dctTriangles = { color: sum(notOnSameLine(*threePts) for threePts in combinations(lst, 3)) for color,lst in dctPts.items() }
    maxTriangles = max(dctTriangles.values())
    
    return [len(input_),
            len(dctPts),
            sum(dctTriangles.values()),
            sorted(color for color,n in dctTriangles.items() if n == maxTriangles) + [maxTriangles] if maxTriangles else [] ]