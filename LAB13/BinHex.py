def DecToBin(decimal_var):
    if(decimal_var > 1):
        DecToBin(decimal_var//2)

    print(decimal_var % 2, end=' ')

def GetTheChar(decimal_var):
    if decimal_var < 10:
        help_var = decimal_var
    elif decimal_var == 10:
        help_var = 'A'
    elif decimal_var == 11:
        help_var = 'B'
    elif decimal_var == 12:
        help_var = 'C'
    elif decimal_var == 13:
        help_var = 'D'
    elif decimal_var == 14:
        help_var = 'E'
    elif decimal_var == 15:
        help_var = 'F'

    return help_var

def DecToHex(decimal_var):
    while decimal_var > 0:
        hex_var = decimal_var % 16
        decimal_var = decimal_var // 16
        print(GetTheChar(hex_var), end = ' ')

def BinToDec(binary_var):
    decimal_var, i, n = 0, 0, 0

    while binary_var != 0:
        dec = binary_var % 10
        decimal_var += dec * pow(2, i)
        binary_var = binary_var // 10
        i += 1
    
    return decimal_var

def HexToDec(hex_var):
    conversion_table = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }

    dec_var = 0
    power = len(hex_var) - 1

    for any_digit in hex_var:
        dec_var += conversion_table[any_digit] * 16 ** power
        power -= 1

    return dec_var
