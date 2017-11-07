# coin sums

from __future__ import print_function

target = 200
coins = [1,2,5,10,20,50,100,200]
ways = [1] + [0]*200

for coin in coins:
    for i in range(coin,target+1):
        ways[i] += ways[i-coin]

print(ways[target])
