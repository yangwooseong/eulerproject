from __future__ import print_function
import math

ss = 0
for i in range(2,499999):
    c = i
    s = 0
    while i != 0:
        s += pow(i % 10,5)
        i = i // 10
    if s == c:
        print (c)
        ss += c

print(ss)
