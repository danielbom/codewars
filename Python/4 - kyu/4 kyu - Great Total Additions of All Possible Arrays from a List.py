# https://www.codewars.com/kata/great-total-additions-of-all-possible-arrays-from-a-list/train/python
# My solution
import itertools
def make_sequence(n, *args):
    digits = map(str,args)
    iter_digits = itertools.izip_longest(*digits, fillvalue='')
    result = []
    d = set()
    for i in iter_digits:
        for j in "".join(i):
            if j not in d:
                d.add(j)
                result.append(int(j))
    return result[:n]

def gta(limit, *args):
    sequence = make_sequence(limit, *args)
    return sum(sum(x) for i in range(1, limit+1) for x in itertools.permutations(sequence,i))

# ...
from itertools import izip_longest
def gta(limit, *args):
    ds = [int(c)
        for t in izip_longest(*map(str, args), fillvalue='')
        for c in t if c]
    ds = sorted(set(ds), key=ds.index)[:limit]
    nn = 0
    np = 1
    for i in range(1, limit + 1):
        nn += np * i
        np *= limit - i
    return nn * sum(ds)

# ...
from itertools import imap, izip_longest, permutations
def gta(limit, *args):
    return sum(sum(p) for i in xrange(1, limit+1) for p in permutations(mkList(limit, args), i))

def mkList(limit, args):
    seen, zs = set(), izip_longest(*(imap(str, args)))
    return [int(i) for z in zs for i in z if i and not (i in seen or seen.add(i))][:limit]