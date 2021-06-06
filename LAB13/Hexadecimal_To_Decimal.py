from BinHex import HexToDec

hexadecimal = str (input ('Podaj liczbe szesnastkowa: '))
strend = 'Liczba {} w systemie dziesiętnym to {}'

decimal = HexToDec(hexadecimal)

print(strend.format(hexadecimal, decimal))
