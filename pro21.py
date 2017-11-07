from __future__ import print_function

def divisors(n):
    divs = []
    r = 2
    p = 0
    while n!= 1 :
        if n % r == 0:
            n = n/r
            p += 1
            if n % r != 0:
                divs.append(r**p)
                p = 0
        else:
            r += 1
    return divs

def getCopy(lists):
    for i in len(lists):
        div[i] = lists[i]

for n in range(2,10000):
    divs = divisors(n)
    div = getCopy(divs)

    if len(divs) == 1:
        continue
    for i in range(2,len(divisors(n))-1):
        for j in range(2,len(divisors(n))):
            if (i*j-1)
            
     
