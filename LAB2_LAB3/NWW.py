a = int (input ('Podaj pierwsza liczbe:\n'))
b = int (input ('Podaj druga liczbe:\n'))
aa = a
bb = b

while a != b:
    if a > b:
        a -= b
    
    else:
        b -= a

c = aa / a * bb
nww = 'Najmniejsza wspolna wielokrotnosc to'
print (nww, int (c))
