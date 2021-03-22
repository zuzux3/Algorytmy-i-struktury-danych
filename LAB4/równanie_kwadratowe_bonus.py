import cmath
import math

a = float (input ("Podaj wartosc a:"))
b = float (input ("Podaj wartosc b:"))
c = float (input ("Podaj wartosc c:"))

if a == 0:
    wynik = "Podane rownanie nie jest rownaniem kwadratowym!\n"
    print(wynik)

else:
    delta = b ** 2 - 4 * a * c
    
    if delta == 0:
        x = -b / 2 * a
        wynik = "x wynosi {}\n"
        print(wynik.format(x))
    
    elif delta > 0:
        x = (-b - math.sqrt(delta)) / 2 * a
        xx = (-b + math.sqrt(delta)) / 2 * a
        wynik = "x zawiera się w przedziale {} i {}\n"
        print(wynik.format(x, xx))

    elif delta < 0:
        uwaga = "Brak rozwiazan rzeczywistych\nProgram obliczy wartosc zespolona!\n"
        print(uwaga)
        x = (-b - cmath.sqrt(delta)) / 2 * a
        xx = (-b + cmath.sqrt(delta)) / 2 * a
        wynik = "x zawiera sie w przedziale {} i {}\n"
        print(wynik.format(x, xx))
    
    else:
        wynik = "Blad programu!\nDelta nie spelnia zadnego warunku!\n"
        print(wynik)
