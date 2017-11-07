# Permuted multiples

from __future__ import print_function
import itertools

def getSup(d):
    return 10**d + 7*10**(d-1)

d = 2
n = 10**d

while True:
    
    multiples = [2*n,3*n,4*n,5*n,6*n]
    if all(str(i) in [''.join(j) for j in  itertools.permutations(str(n))] \
               for i in multiples):
        print(n)
        break
    if n > getSup(d):
        d += 1
        n = 10**d
    else:
        n += 1
