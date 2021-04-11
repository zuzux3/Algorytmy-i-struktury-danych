wiersze = int (input ("Podaj ilosc wierszy: "))
kolumny = int (input ("Podaj ilosc kolumn: "))
macierz1 = []
macierz2 = []
dane1 = "Podaj dane pierwszej macierzy wierszami:\n"
dane2 = "Podaj dane drugiej macierzy wierszami:\n"

print (dane1)
for i in range (wiersze):
    a1 = []
    for j in range (kolumny):
        a1.append (int (input ()))
    macierz1.append(a1)

print (dane2)
for i in range (wiersze):
    a2 = []
    for j in range (kolumny):
        a2.append (int (input ()))
    macierz2.append(a2)

wynik = [[macierz1[i][j] - macierz2[i][j] for j in range (len (macierz1[0]))] for i in range (len(macierz1))]

print("Wynik odejmowania podanych macierzy:\n")
for w in wynik:
    print (w)
