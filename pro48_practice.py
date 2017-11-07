# self powers

from __future__ import print_function

sm = 0
N = 1000

for i in range(1,N+1):
    m = i**i
    sm = (sm + m) % (10**10)

print(sm)
