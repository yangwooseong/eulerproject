# self powers

from __future__ import print_function

sm = 0
N = 1000

for i in range(1,N+1):
    m = 1
    for j in range(i):
        m = (m * i) % (10**10)
    sm = (sm + m) % (10**10)

print(sm)
