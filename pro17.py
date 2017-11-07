from __future__ import print_function

num = range(1,20) + range(20,91,10)
strnum = 'one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety'.split()

print (num)

n = 0

def count(i):
    count = 0
    if i in num:
        count += len(strnum[(num.index(i))])
    else:
        j = i / 10 # 10 digit
        k = i % 10 # 1 digit
        count += len(strnum[(num.index(10*j))]) + len(strnum[(num.index(k))])
    return (count)

for i in range(1,1000):
    if i in range(1,100):
        n += count(i)
    elif i % 100 == 0:
        n += len(strnum[(num.index(i/100))]) + len('hundred')
    else:
        l = i / 100
        k = i % 100
        n += len(strnum[(num.index(i/100))]) + len('hundred') + len('and')
        n += count(k)

n += len('onethousand')
print(n)

s = 0
for i in range(1,100):
    s += count(i)
    print (s,i)
    
