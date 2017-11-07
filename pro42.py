# triangle numbers

import string

def wordvalue(word):
    alphabets = list(string.ascii_uppercase)
    value = 0
    for symbol in word:
        value += alphabets.index(symbol)+1
    return value

SUP = 20

words = open('pro42_word.txt').read().rstrip().split(",")
for i in range(len(words)):
    words[i] = words[i][1:-1]
triwords = map(lambda(x):x*(x+1)/2,range(1,SUP+1))

s = 0
for i in range(len(words)):
    if wordvalue(words[i]) in triwords:
        s += 1
    elif wordvalue(words[i]) > max(triwords):
        print('SUP is not good')

print(s)
