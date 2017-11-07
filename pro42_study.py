# triangle numbers

import string
import math

is_tn = lambda t: (-1+math.sqrt(1+8*t))/2 % 1 == 0
score = lambda word:sum(ord(symbol)-ord('A')+1 for symbol in word)

words = open('pro42_word.txt').read().rstrip().split(",")

print sum(is_tn(score(word[1:-1])) for word in words)
