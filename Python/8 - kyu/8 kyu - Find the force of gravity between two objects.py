# https://www.codewars.com/kata/find-the-force-of-gravity-between-two-objects/train/python
# My solution
from decimal import Decimal

def convert(val, unit, units, conv):
    for i in range(len(units)):
        if unit == units[i]:
            return val / Decimal(conv[i])
    
def solution(val, unit) :
    val = list(map(Decimal, val))
    val[0] = convert(val[0], unit[0], ["kg", "g", "mg", "μg", "lb"], [1, 1e3, 1e6, 1e9, 1/0.453592])
    val[1] = convert(val[1], unit[1], ["kg", "g", "mg", "μg", "lb"], [1, 1e3, 1e6, 1e9, 1/0.453592])
    val[2] = convert(val[2], unit[2], ["m", "cm", "mm", "μm", "ft"], [1, 1e2, 1e3, 1e6, 1/0.3048])
    G = Decimal(6.67 * 1e-11)
    F = (G * val[0] * val[1]) / (val[2] * val[2])
    return float(F)

# ...
units = {"kg": 1, "g": 1e-3, "mg": 1e-6, "μg": 1e-9, "lb": 0.453592,
         "m": 1, "cm": 1e-2, "mm": 1e-3, "μm": 1e-6, "ft": 0.3048,
         "G": 6.67e-11}

def solution(v, u):
    m1, m2, r = (v[i] * units[u[i]] for i in range(3))
    return units["G"] * m1 * m2 / r**2

# ...
d, m = {
    'm': 1,
    'cm': 1/100,
    'mm': 1/1_000,
    'μm': 1/1_000_000,
    'ft': 0.3048,
}, {
    'kg': 1,
    'g': 1/1_000,
    'mg': 1/1_000_000,
    'μg': 1/1_000_000_000,
    'lb': 0.453592,
}
G = 6.67 / 10 ** 11

def solution(a, b) :
    m1 = a[0] * m[b[0]]
    m2 = a[1] * m[b[1]]
    r = a[2] * d[b[2]]
    return G * m1 * m2 / r**2

# ...
from itertools import starmap

G = 6.67e-11
CONVERSIONS = {'cm': 1e-2, 'mm': 1e-3, 'μm': 1e-6, 'ft': 0.3048,
               'g':  1e-3, 'mg': 1e-6, 'μg': 1e-9, 'lb': 0.453592}

def solution(a,b):
    m1, m2, d = starmap(lambda v,u: v * CONVERSIONS.get(u,1), zip(a,b))
    return G * m1 * m2 / (d*d)