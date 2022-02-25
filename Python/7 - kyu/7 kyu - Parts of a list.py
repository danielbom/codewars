# https://www.codewars.com/kata/parts-of-a-list/train/python
# My solution
def partlist(arr):
    return [(' '.join(arr[:i]), ' '.join(arr[i:]) ) for i in range(1, len(arr)) ]

