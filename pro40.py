# Champernowne's constant

from __future__ import print_function

def champer(n):
    i = 1
    while n > 0:
        m = list(str(i))[::-1]
        while m != [] and n > 0:
            yield int(m.pop())
            n -= 1
        i += 1

p = 0
mul = 1
th = 1

for i in champer(1000000):
    if th == 10**p:
        print(i)
        mul = mul * i
        p += 1
    th += 1

print(mul)
