# https://www.codewars.com/kata/the-supermarket-queue/train/python
# My solution
def queue_time(customers, n):
    if not customers: return 0
    finished = 0
    time = -1
    while len(customers) > finished:
        k = 0
        for i in range(len(customers)):
            if customers[i] > 0:
                customers[i] -= 1
                k += 1
            elif customers[i] == 0:
                customers[i] -= 1
                finished += 1
            if k == n:
                break
        time += 1
    return time

# Other ways
def queue_time(customers, n):
    l=[0]*n
    for i in customers:
        l[l.index(min(l))]+=i
    return max(l)

# ...
import heapq

def queue_time(customers, n):
    heap = [0] * n
    for time in customers:
        heapq.heapreplace(heap, heap[0] + time)
    return max(heap)