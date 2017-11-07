def Nthprime(N):
    if N == 1:
        return 2
    else:
        p = 3
        while N > 1 :
            n = 3
            while n*n <= p:
                if p % n == 0:
                    break
                n +=1
            if n*n > p:
                N -= 1
            if N ==1:
                return p
            p += 2

N = int(raw_input('type a positive integer: '))
print Nthprime(N)
