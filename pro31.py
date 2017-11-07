# coin sums

from __future__ import print_function

money = 200
coins = [200,100,50,20,10,5,2,1]

way = 0
A,B,C,D,E,F,G,H = 2,3,5,11,21,41,101,201

for a in range(0,2):
    for b in range(0,2*(1-a)+1):
        for c in range(0,(200-200*a-100*b)/50+1):
            for d in range(0,(200-200*a-100*b-50*c)/20+1):
                for e in range(0,(200-200*a-100*b-50*c-20*d)/10+1):
                    for f in range(0,(200-200*a-100*b-50*c-20*d-10*e)/5+1):
                        for g in range(0,(200-200*a-100*b-50*c-20*d-10*e-5*f)/2+1):
                            for h in range(0,H):
                                if 200*a+100*b+50*c+20*d+10*e+5*f+2*g+h == money:
                                    way += 1

print(way)
