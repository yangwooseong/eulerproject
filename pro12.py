from __future__ import print_function

def divisors(n):
    divs = 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            divs += 2
    return divs - (1 if (int(n**0.5))**2 == n else 0)

n = 1
while True:
    tri = (n*(n+1)/2)
    if divisors(tri)>500:
        print(tri)
        break
    n += 1
    
