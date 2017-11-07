from __future__ import print_function

def factorial(n):
    return n*factorial(n-1) if n >= 2 else 1

def perm(L,n):
    if len(L) == 1:
        return L
    else:
        q,r = divmod(n,factorial(len(L)-1))
        a = L[q]
        return [a] + perm(L[:q]+L[q+1:],r)
        
L = range(4)
print(perm(L,1))
