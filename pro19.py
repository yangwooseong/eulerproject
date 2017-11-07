months = [31,28,31,30,31,30,31,31,30,31,30,31]
monthss = []

for i in range(len(months)):
    monthss.append(months[i])

monthss[1] = 29

s = 1
num = 0
for i in range(1,101):
    if i % 4 == 0:
        for j in monthss:
            s += j
            if s%7 == 6:
                num += 1
                print (s,num,s%7)
    else:
        for j in months:
            s += j
            if s%7 == 6:
                num += 1
                print (s,num,s%7)
print (s,num)
