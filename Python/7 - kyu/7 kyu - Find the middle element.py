# https://www.codewars.com/kata/545a4c5a61aa4c6916000755/train/python
# My solution
def gimme(array):
    def _gimme(array):
        n = len(array)
        if n == 1 or n == 2:
            val = min(array)
            return val[1]

        array.remove(min(array))
        array.remove(max(array))
        return _gimme(array)

    return _gimme([(x, i) for i, x in enumerate(array)])

# ...
def gimme(lst):
    return lst.index(sorted(lst)[len(lst)//2])
