from __future__ import print_function

def factorial(n):
    return n*factorial(n-1) if n >= 2 else 1

def perm(L,n):
    if n == 1:
        return L
    elif n == factorial(len(L)):
        return L[::-1]
    else:
        m = n / factorial(len(L)-1)
        if n % factorial(len(L)-1) == 0:
            a = L[m-1]
            L.remove(a)
            return [a] + perm(L ,factorial(len(L)))
        else:
            a = L[m]
            L.remove(a)
            return [a] + perm(L, n % factorial(len(L)))

L = range(10)
print(perm(L,1000000))
