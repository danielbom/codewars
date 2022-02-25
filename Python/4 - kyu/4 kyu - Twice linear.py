# https://www.codewars.com/kata/twice-linear/train/python
# My solution
def dbl_linear(n):
    f = lambda x: (2*x+1, 3*x+1)
    r = {1: f(1)}
    while len(r) < n * 4:
        for key, value in list(r.items()):
            if value != True:
                v2 = value[0]
                v3 = value[1]
                r[v2] = f(v2)
                r[v3] = f(v3)
                r[key] = True
    s = set()
    for key, value in r.items():
        s.add(key)
        if isinstance(value, tuple):
              s.add(value[0])
              s.add(value[1])
    s = list(s)
    s.sort()
    return s[n]

# ...
from collections import deque
def dbl_linear(n):
    h = 1; cnt = 0; q2, q3 = deque([]), deque([])
    while True:
        if (cnt >= n):
            return h
        q2.append(2 * h + 1)
        q3.append(3 * h + 1)
        h = min(q2[0], q3[0])
        if h == q2[0]: h = q2.popleft()
        if h == q3[0]: h = q3.popleft()
        cnt += 1


# ...
from collections import deque
def dbl_linear(n):
    u, q2, q3 = 1, deque([]), deque([])
    for _ in range(n):
        q2.append(2 * u + 1)
        q3.append(3 * u + 1)
        u = min(q2[0], q3[0])
        if u == q2[0]: q2.popleft()
        if u == q3[0]: q3.popleft()
    return u

# ...
from bisect import insort
def dbl_linear(n):
    u = [1]
    u0 = 123
    for i in range(n):
        while u[0] == u0:
            u.pop(0)
        u0 = u.pop(0)
        insort(u, 2*u0+1)
        insort(u, 3*u0+1)
    return u[0]

# ...
from heapq import heappush, heappop
def dbl_linear(n):
    uncalc = [1]
    uncalc_set = set([1])

    for i in range(n):
        x = heappop(uncalc)
        uncalc_set.remove(x)

        y = 2 * x + 1
        z = 3 * x + 1

        # ensure y not already recorded
        if y not in uncalc_set:
            heappush(uncalc, y)
            uncalc_set.add(y)

        heappush(uncalc, z)
        uncalc_set.add(z)

    return heappop(uncalc)