from __future__ import print_function

def factorial(n):
    return reduce(lambda x,y:x*y,xrange(1,n+1),1)

n = factorial(100)

s = sum(map(int,str(n)))
print (s)
