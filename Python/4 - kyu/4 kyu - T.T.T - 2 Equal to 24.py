# https://www.codewars.com/kata/574be65a974b95eaf40008da/train/python
# My solution
from itertools import product, permutations

DICT_OPS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "/": lambda a, b: a / b,
    "*": lambda a, b: a * b,
}

def math_expr(keys_ops, values, direction):
    a, b, c, d = values
    o, p, q = keys_ops
    join = lambda *xs: "".join(str(x) for x in xs)
    
    def math_expr_middle():
        return join("(", a, o, b, ")", p, "(", c, q, d, ")")

    def math_expr_right():
        return join("((", a, o, b, ")", p, c, ")", q, d)
    
    def math_expr_left():
        return join(a, o, "(", b, p, "(", c, q, d, "))")
    
    directions = { "middle": math_expr_middle, "right": math_expr_right, "left": math_expr_left }
    return directions[direction]()

def compute(ops, values, direction):
    def reject(fn):
        def inner(*args, **kargs):
            try:
                return fn(*args, **kargs)
            except:
                return 0
        return inner

    a, b, c, d = values
    o, p, q = ops
    compute_middle = reject(lambda: p(o(a, b), q(c, d)))
    compute_right = reject(lambda: q(p(o(a, b), c), d))
    compute_left = reject(lambda: o(a, p(b, q(c, d))))
    
    directions = { "middle": compute_middle, "right": compute_right, "left": compute_left }
    return directions[direction]()

def check(keys_ops, values):
    ops = [DICT_OPS[key] for key in keys_ops]
    directions = ["middle", "right", "left"]
    for direction in directions:
        result = compute(ops, values, direction)
        parts = divmod(result, 1)
        if parts == (24, 0):
            return math_expr(keys_ops, values, direction)

def equal_to_24(a,b,c,d):
    list_ops = list(DICT_OPS.keys())
    product_ops = list(product(list_ops, repeat=3))
    permutations_values = list(permutations([a, b, c, d]))
    for new_values in permutations_values:
        for keys_ops in product_ops:
            result = check(keys_ops, new_values)
            if result:
                return result
    return "It's not possible!"

# ...
from itertools import permutations

def equal_to_24(*aceg):
    ops = '+-*/'
    
    for b in ops:
        for d in ops:
            for f in ops:
                for (a,c,e,g) in permutations(aceg):
                    for s in make_string(a,b,c,d,e,f,g):
                        try:
                            if eval(s + '== 24'):
                                return s
                        except:
                            pass
                            
    return "It's not possible!"

def make_string(a,b,c,d,e,f,g):
    return [f"(({a} {b} {c}) {d} {e}) {f} {g}",
            f"({a} {b} {c}) {d} ({e} {f} {g})",
            f"{a} {b} ({c} {d} ({e} {f} {g}))"]

# ...
from functools import lru_cache as memo
from itertools import permutations, product
from operator import add, sub, mul, truediv as div
operators = {add: '+', sub: '-', mul: '*', div: '/'}

@memo(None)
def evaluate_tree(terms, ops):
    if not ops: return {terms[0]: str(terms[0])}
    results = {}
    for idx, op in enumerate(ops, 1):
        left, right = evaluate_tree(terms[:idx], ops[:idx-1]), evaluate_tree(terms[idx:], ops[idx:])
        results.update({op(l, r): f'({left[l]}){operators[op]}({right[r]})'
                        for l, r in product(left, right) if not (op == div and r == 0)})
    return results

def equal_to_24(*terms):
    for operands in permutations(terms):
        for ops in product(operators, repeat=3):
            results = evaluate_tree(operands, ops)
            if 24 in results: return results[24]
    return "It's not possible!"

# ...
import itertools as it

def equal_to_24(*numbers):
    for template in ["aZ(bX(cVd))", "(aZb)X(cVd)", "((aZb)Xc)Vd"]:
        for x in it.permutations(numbers):
            for i in it.product('*/+-', repeat=3):
                temp = template
                for r in (("Z", i[0]), ("X", i[1]), ("V", i[2]), ("a", str(x[0])), ("b", str(x[1])), ("c", str(x[2])),
                          ("d", str(x[3]))):
                    temp = temp.replace(*r)
                try:
                    if (eval(temp) == 24):
                        return temp
                except ZeroDivisionError:
                    pass
    return "It's not possible!"

# ...
import operator
from itertools import product, permutations

def mydiv(n, d):
    return n / d if d != 0 else 9999999

syms = [operator.add, operator.sub, operator.mul, mydiv]
op = {sym: ch for sym, ch in zip(syms, '+-*/')}

def solve24(nums):
    for x, y, z in product(syms, repeat=3):
        for a, b, c, d in permutations(nums):
            if round(x(y(a, b), z(c, d)), 5) == 24:
                return f"({a} {op[y]} {b}) {op[x]} ({c} {op[z]} {d})"
            elif round(x(a, y(b, z(c, d))), 5) == 24:
                return f"{a} {op[x]} ({b} {op[y]} ({c} {op[z]} {d}))"
            elif round(x(y(z(c, d), b), a), 5) == 24:
                return f"(({c} {op[z]} {d}) {op[y]} {b}) {op[x]} {a}"
            elif round(x(y(b, z(c, d)), a), 5) == 24:
                return f"({b} {op[y]} ({c} {op[z]} {d})) {op[x]} {a}"
    return "It's not possible!"

def equal_to_24(a, b, c, d):
    return solve24([a, b, c, d])

# ...
import requests
import re


def equal_to_24(a, b, c, d):
    text = requests.get(f"http://scripts.cac.psu.edu/staff/r/j/rjg5/scripts/Math24.pl?a={a}&b={b}&c={c}&d={d}").text
    a = re.findall(r"(.*)=(.*)<br>", text)
    for i in a:
        return i[0].strip()
    return "It's not possible!"

# ...
