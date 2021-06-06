from BinHex import DecToBin, DecToHex

decimal = int (input ('Podaj liczbe dziesietna: '))
str_end1 = "Liczba {} w systemie binarnym to:"
str_end2 = ",\na w systemie szesnastkowym to: "

print(str_end1.format(decimal))
DecToBin(decimal)
print(str_end2)
DecToHex(decimal)
