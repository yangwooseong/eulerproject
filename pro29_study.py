# distinct powers

from __future__ import print_function
import math

L = 100
r = range(2,L+1)

print(len(set(a**b for a in r for b in r)))
