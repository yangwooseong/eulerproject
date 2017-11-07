# sum of sprial diagonals

from __future__ import print_function

def spiralNum(n):
    num = 1
    dif = 2
    while True:
        for s in range(4):
            if n > 0:
                yield num
                num += dif
                n -= 1
        dif += 2 
        if n == 0:
            break

s = 0
for i in spiralNum(2*1001-1):
    s += i
    print(i)

print(s)
