from BinHex import BinToDec

binary = int (input ("Wprowadz liczbe binarna: "))

str_end = "Liczba binarna {} w systemie dziesietnym to {}"
decimal = BinToDec(binary)

print(str_end.format(binary, decimal))
