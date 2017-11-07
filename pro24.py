from __future__ import print_function

def factorial(n):
    return n*factorial(n-1) if n >= 2 else 1

perm = ''
lists = range(10)
N = 1000000

for i in range(10)[::-1]:
    a = N/factorial(i)
    if N%factorial(i) != 0:
        perm = perm + str(lists[a])
        del lists[a]
    else:
        perm = perm + str(lists[a-1])
        del lists[a-1]
    print(a,lists,N,perm)
    N = N % factorial(i)

print(perm)

