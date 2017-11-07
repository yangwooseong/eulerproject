listf = []
liste = []

a = 1
b = 2

while True :
    listf.append(a)
    listf.append(b)
        
    if a % 2 == 0 : 
        liste.append(a)
    if b % 2 == 0 :
        liste.append(b)
        
    if a >= 4000000 or b >= 4000000: break

    a = a + b
    b = a + b

print sum(liste)
print listf
print liste
