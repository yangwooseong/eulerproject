# Champernowne's constant

from __future__ import print_function

lists = [10**p for p in range(2,7)]

for i in lists:
    j = 1
    s, f = 1,9
    while i not in range(s,f+1):
        j += 1
        s = f + 1
        f += (j)*(10**j-10**(j-1))
    i -= (s-1)
    (q,r) = divmod(i,j)
    if r == 2:
        r = 3
    print(i,str(10**(j-1)+q)[r-1])
