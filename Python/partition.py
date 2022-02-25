# https://www.codewars.com/kata/55cf3b567fc0e02b0b00000b/train/python

cache = { 1: [[1]] }

def enum(n, x=None):
    if cache.get(n, False):
        return cache[n]

    x = n if x is None else x
    
    f = lambda n: [[n - i, i] for i in range(1, n // 2 + 1)]
    partial1 = f(n)
    partial2 = []
    for p in partial1:
        for i, e in enumerate(p):
            if e > 1:
                nested = [sorted(r + p[i+1:], reverse=True) for r in enum(e, n)[1:]]
                partial2 += [k for k in nested if sum(k) == n]

    s = set()
    result = [[n]] + partial1
    for i, r in enumerate(map(tuple, partial2)):
        if r not in s:
            result.append(partial2[i])
        s.add(r)

    cache[n] = result
    return result

for i in range(1, 6):
    print(enum(i))

def part(n):
    partition = enum(n)
    prod = [sum(p) for p in partition]
    r = max(prod) + min(prod)
    a = sum(prod) / len(prod)
    m = sorted(prod)[len(prod) // 2]
    return "Range: {:.2f} Average: {:.2f} Mediam: {:.2f}".format(r, a, m)
    
