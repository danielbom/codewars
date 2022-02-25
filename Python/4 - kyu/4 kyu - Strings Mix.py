# https://www.codewars.com/kata/strings-mix/train/python
# My solution
from collections import Counter
from operator import itemgetter

def mix(s1, s2):
    remove_ones = lambda dict_: {k:v for k,v in dict_.items() if v > 1 }
    s1 = remove_ones(Counter(filter(str.islower, s1)))
    s2 = remove_ones(Counter(filter(str.islower, s2)))
    letters = set(s1.keys()).union(s2.keys())
    r = sorted((('1',l,s1.get(l,0)) if s1.get(l,0) > s2.get(l,0) else
         ('2',l,s2.get(l,0)) if s2.get(l,0) > s1.get(l,0) else
         ('=',l,s1.get(l,0)) for l in letters), key=itemgetter(0,1))
    r.sort(key=itemgetter(2), reverse=True)
    return "/".join(map(lambda v: "{winner}:{null:{letter}^{times}s}".format(winner=v[0], letter=v[1], times=v[2], null='') ,r))

# ...
from collections import Counter
def mix(s1, s2):
    c1 = Counter(filter(str.islower, s1))
    c2 = Counter(filter(str.islower, s2))
    res = []
    for c in set(c1.keys() + c2.keys()):
        n1, n2 = c1.get(c, 0), c2.get(c, 0)
        if n1 > 1 or n2 > 1:
            res.append(('1', c, n1) if n1 > n2 else
                ('2', c, n2) if n2 > n1 else ('=', c, n1))
    res = ['{}:{}'.format(i, c * n) for i, c, n in res]
    return '/'.join(sorted(res, key=lambda s: (-len(s), s)))

# ...
def mix(s1, s2):
    hist = {}
    for ch in "abcdefghijklmnopqrstuvwxyz":
        val1, val2 = s1.count(ch), s2.count(ch)
        if max(val1, val2) > 1:
            which = "1" if val1 > val2 else "2" if val2 > val1 else "="
            hist[ch] = (-max(val1, val2), which + ":" + ch * max(val1, val2))
    return "/".join(hist[ch][1] for ch in sorted(hist, key=lambda x: hist[x]))

# ...
def mix(s1, s2):
    output = []
    for char in {c for c in s1 + s2 if c.islower()}:
        check = s1.count(char), s2.count(char)
        m = max(check)
        if m > 1:
            output += ["=12"[cmp(*check)] + ":" + m * char]
    output.sort(key = lambda x: (-len(x), x))
    return '/'.join(output)

# ...
from collections import Counter
def mix(s1, s2):
    c1, c2 = [Counter({s: n for s, n in Counter(c).items() if n > 1 and s.islower()}) for c in (s1, s2)]
    return '/'.join(c + ':' + -n * s for n, c, s in
                    sorted((-n, '=12'[(c1[s] == n) - (c2[s] == n)], s) for s, n in (c1 | c2).items()))

# ...
mix=lambda a,b:'/'.join(sorted(("=12"[cmp(*k)]+":"+max(k)*r
    for r,k in{(c, (a.count(c), b.count(c)))
    for c in a+b if c.islower()}if max(k)>1),
    key=lambda x:(-len(x),x)))

# ...
from collections import Counter
def mix(s1, s2):
    res = []
    c1 = Counter([c for c in s1 if c.islower()])
    c2 = Counter([c for c in s2 if c.islower()])
    for c in c1 | c2:       
        if c1[c] > 1 and c1[c] > c2[c]: res += ['1:' + c * c1[c]]
        if c2[c] > 1 and c2[c] > c1[c]: res += ['2:' + c * c2[c]]
        if c1[c] > 1 and c1[c] == c2[c]: res += ['=:' + c * c1[c]]
    return '/'.join(sorted(res, key = lambda a : [-len(a), a]))