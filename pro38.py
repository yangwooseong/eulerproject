# Pandigital multiples

from __future__ import print_function

def pandigital(n):
    if len(str(n)) == 9 and \
            all (i in str(n) for i in '123456789'):
        return True
    else:
        return False

pandigitals = []

for i in range(1,9877):
    if i % 10 != 5:
        conc = ''
        for n in range(1,10):
            conc += str(i*n)
            if pandigital(conc):
                pandigitals.append(int(conc))
            elif len(conc) > 10:
                break

print(max(pandigitals))
