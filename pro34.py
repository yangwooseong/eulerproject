from __future__ import print_function

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n*factorial(n-1)

faclist = map(factorial,range(10))

i = 12
s = 0
while i < factorial(9)*7: 
    sum = 0
    g = map(int,list(str(i)))
    for k in g:
        sum += faclist[k]
    if i == sum:
        s += i
    i += 1

print(s)
