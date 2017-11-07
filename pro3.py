import math

i = 2

#num = 13195
num = 600851475143
lists = []

while i <= int(math.sqrt(num)):
    for j in lists:
        if i % j == 0:
            break
    if num % i == 0: 
        lists.append(i)
        for j in lists:
            if i % j == 0 and i != j:
                lists.remove(i)
                break
    i = i + 1
    
print lists
