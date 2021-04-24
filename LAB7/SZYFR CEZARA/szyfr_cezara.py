import coding_and_decoding_caesar

choosing = str (input ('Wypisz: Chcesz coś zaszyfrować (wpisz: 1) lub zdekodować (wpisz: 0): '))

if choosing == '1':
    text = str (input ('Podaj tekst do zaszyfrowania:\n'))
    text = text.lower()
    code = coding_and_decoding_caesar.coding(text)
    ending_str = 'Zaszyfrowany tekst:\n{}'
    
    print(ending_str.format(code))

elif choosing == '0':
    text = str (input ('Podaj tekst do odszyfrowania:\n'))
    text = text.lower()
    decode = coding_and_decoding_caesar.decoding(text)
    ending_str = 'Odszyfrowany tekst:\n{}'

    print(ending_str.format(decode))

else:
    ending_str = "Wrong input"

    print(ending_str)
