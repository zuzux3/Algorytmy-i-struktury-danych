a = int ( input('Podaj pierwsza liczbe:\n'))
b = int ( input('Podaj druga liczbe:\n'))

while a != b:
    if a > b:
        a -= b

    else:
        b -= a

nwd = "Najwiekszy wspolny dzielnik to "
print (nwd, a)
