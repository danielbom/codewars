# https://www.codewars.com/kata/fold-an-array/train/python
# My solution
from itertools import zip_longest

def fold_array( array, runs ):
    if runs == 0 or len( array ) <= 1:
        return array
    length = len( array )
    n = length // 2 + ( length % 2 != 0 )
    split = zip_longest( array[:n], reversed(array[n:]), fillvalue=0 )
    folded = [ x+y for x,y in split ]
    return fold_array( folded, runs-1 )

# ...
def fold_array(array, runs):
    nums = list(array)
    for _ in xrange(runs):
        for a in xrange(len(nums) // 2):
            nums[a] += nums.pop()
    return nums

# ...
def fold(arr):
    length = len(arr)
    mid = length // 2
    return [a + b for a, b in zip(arr, arr[-1:-mid-1:-1])] + [arr[mid]] * (length & 1)
    
def fold_array(array, runs):
    ret = array
    for __ in range(runs):
        ret = fold(ret)
    return ret

# ...
def fold_array(arr, runs):
    center, mod = divmod(len(arr), 2)
    arr_left = arr[:center]
    arr_right = arr[center+mod:]
    tail = [arr[center]] * mod
    folded = [sum(i) for i in zip(arr_left, arr_right[::-1])] + tail
    return folded if runs == 1 else fold_array(folded, runs - 1)

# ...
from itertools import zip_longest
from functools import reduce
def fold_array(array, runs):
    f = lambda x, y: [a + b for a, b in zip_longest(x[:len(x)//2], reversed(x[len(x)//2:]), fillvalue=0)]
    return reduce(f, range(runs), array)