liczba = int (input ("Podaj liczbe naturalna wieksza lub rowna 2\n"))
i = 2

if liczba >= 2:
    if liczba == 2:
        pierwsza = True

    else:
        while i < liczba:
            if liczba % i == 0:
                pierwsza = False
                break

            pierwsza = True
            i += 1

else:
    zle = 'Podano liczbe mniejsza od 2\n'
    print (zle)

if pierwsza == True:
    wynik = 'Podana liczba jest liczba pierwsza.\n'
    print (wynik)

else:
    wynik = 'Podana liczba nie jest liczba pierwsza.\n'
    print (wynik)
