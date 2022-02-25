# https://www.codewars.com/kata/best-travel/train/python
# My solution
from itertools import combinations

def choose_best_sum(t, k, lst):
    return None if k > len(lst) else max([sum(i) for i in combinations(lst, k) if sum(i) <= t], default=None)
# ...
from itertools import combinations

def choose_best_sum(t, k, ls):
    return max((s for s in map(sum, combinations(ls,k)) if s <= t), default=None)
# ...
from itertools import combinations

def choose_best_sum(t, k, ls):
    return max((sum(v) for v in combinations(ls,k) if sum(v)<=t), default=None)
# ...
from itertools import combinations

def choose_best_sum(t, k, ls):
    return max((s for s in (sum(dists) for dists in combinations(ls, k)) if s <= t), default=None)
# ...
from itertools import combinations

def choose_best_sum(t, k, ls):
    return max([sum(comb)
                for comb in combinations(ls, k)
                if sum(comb) <= t] or [None])
# ...
import itertools

def choose_best_sum(t, k, ls):
    sums = filter(lambda x: x <= t, map(sum, itertools.combinations(ls, k)))
    if sums:
        return max(sums)
    return None