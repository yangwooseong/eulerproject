NUM = 100

i = 1
lists = []

while i <= NUM:
    lists.append(i*i) 
    if i == NUM :
        print pow(i*(i+1)/2, 2)
        print sum(lists)
        print pow(i*(i+1)/2,2)-sum(lists)
    i += 1
