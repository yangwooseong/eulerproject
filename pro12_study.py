from __future__ import print_function

def divisors(n):
    divs = 0
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            divs += 2
    return divs - (1 if (int(n**0.5))**2 == n else 0)

n = 1
divs = 0
while divs <= 500:
    if n % 2 = 0:
        divs = divisors(n/2)*divisors(n+1) 
    else:
        divs = divisors(n)*divisors((n+1)/2)
    n += 1

tri = n*(n+1)/2
print(tri) 
