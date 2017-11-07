# Permuted multiples

from __future__ import print_function

f = lambda n:sorted(str(n))

n = 102
while not f(n*2) == f(n*3) == f(n*4) == f(n*5) == f(n*6): n += 3

print(n)
