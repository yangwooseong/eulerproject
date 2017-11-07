# Integer right triangles

from __future__ import print_function

def pythatriple(n):
    # find a pythagorean triple whose sum is n
    triples = []
    # two for loops -> a bit slow perfomance
    for t in range(1,n//2+1):
        for s in range(1,t+1):
            if (t % 2 == 0 or s % 2 == 0) and (n-2*(t+s))%3 == 0:
                    r = (n-2*(t+s))/3
                    if r>0 and r**2 == 2*t*s:
                        triples.append((r+s,r+t,r+s+t))
    return len(triples)

num = 0
# if p has n solutions, 2p has n ones or more
for i in range(500,1001,2):
    if num < pythatriple(i):
        num = pythatriple(i)
        p = i
print(num,p)
