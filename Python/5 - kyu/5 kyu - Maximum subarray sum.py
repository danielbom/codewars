# https://www.codewars.com/kata/maximum-subarray-sum/train/python
# My solution
def maxSequence(arr):
    if not arr: return 0
    max_ending = max_current = arr[0]
    
    for i in arr[1:]:
        max_ending = max(i, max_ending + i)
        max_current = max(max_current, max_ending)
    
    return  max_current if max_current > 0 else 0

# ...
def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max

# ...
# cleaner with python 3 and itertools accumulate 
maxSequence = lambda a: max(reduce(lambda (m,r),v: (max(m,r), max(r+v,0)), a, (0,0)))