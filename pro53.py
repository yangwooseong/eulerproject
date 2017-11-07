# Combinatoric selections

def factorial(n):
    return n*factorial(n-1) if n != 0 else 1

def combination(n,r):
    return factorial(n)/(factorial(r)*factorial(n-r))

count = 0
for n in range(23,101):
    for r in range(2,n/2+1):
        if combination(n,r) > 10**6:
            if r*2 != n:
                count += 2
            else:
                count += 1

print(count)
