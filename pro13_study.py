# using map

from __future__ import print_function

g = map(int,(line for line in open('pro13.txt').readlines()))
print(str(sum(g))[:10])
print(g)
