from __future__ import print_function

sum = 0
for line in open('pro13.txt').readlines():
    line = line.rstrip()
    sum = sum + int(line[:14])

print(str(sum)[:10])

