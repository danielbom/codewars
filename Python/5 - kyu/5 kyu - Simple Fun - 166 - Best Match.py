# https://www.codewars.com/kata/simple-fun-number-166-best-match/train/python
# My solution
def best_match(g1, g2):
    mi = 0
    diff = g1[0] - g2[0]
    for i, gs in enumerate(zip(g1,g2)):
        new_diff = gs[0] - gs[1]
        if new_diff == diff and gs[1] > g2[mi]:
            diff = new_diff
            mi = i
        elif new_diff < diff:
            diff = new_diff
            mi = i
    return mi

# ...
def best_match(goals1, goals2):
    return min( (a-b, -b, i) for i,(a,b) in enumerate(zip(goals1, goals2)) )[2]