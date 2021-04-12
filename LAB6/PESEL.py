pesel = str (input ("Podaj nr PESEL: "))
rok = str (input ("Podaj rok urodzenia (w formacie rrrr): "))
miesiac = str (input ("Podaj miesiac urodzenia (w formacie mm): "))
dzien = str (input ("Podaj dzien urodzenia (w formacie dd)"))

a = int (pesel[0])
b = int (pesel[1])
c = int (pesel[2])
d = int (pesel[3])
e = int (pesel[4])
f = int (pesel[5])
g = int (pesel[6])
h = int (pesel[7])
i = int (pesel[8])
j = int (pesel[9])
k = int (pesel[10])
a1 = int (rok[2])
a2 = int (rok[3])
b1 = int (miesiac[0])
b2 = int (miesiac[1])
c1 = int (dzien[0])
c2 = int (dzien[1])

sum = 1 * a  + 3 * b + 7 * c + 9 * d + 1 * e + 3 * f + 7 * g + 9 * h + 1 * i + 3 * j
wynik = 10 - (sum % 10)

if wynik == k:
    if a1 == a and a2 == b:
        if b1 == c and b2 == d:
            if c1 == e and c2 == f:
                pesel_good = "Pesel prawidlowy!\n"
            else:
                pesel_good = "Pesel bledny!\n"
        else:
            pesel_good = "Pesel bledny!\n"
    else:
        pesel_good = "Pesel bledny!\n"
else:
    pesel_good = "Pesel bledny!\n"

print (pesel_good)
