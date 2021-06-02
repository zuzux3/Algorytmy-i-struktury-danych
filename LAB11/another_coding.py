def coding(sentence, lines, columns):
    help_arr = []
    help_str = ''
    a = 0

    for i in range (lines):
        help_arr1 = []

        for j in range (columns):
            help_arr1.append(sentence[a])
            a += 1

        help_arr.append(help_arr1)
    
    for b in range(columns):
        for c in range(lines):
            help_str += help_arr[c][b]
        
    return help_str

lines = int (input ('Podaj liczbe wierszy: '))
columns = int (input ('Podaj liczbe kolumne: '))
length = lines * columns
str1 = 'Podaj zdanie do zaszyfrowania o wielkości {}: '

sentence = str (input (str1.format(length)))

if len(sentence) == length:
    str_end = 'Zaszyfrowane zdanie:\n{}\n'
    sentence = coding(sentence, lines, columns)
    
    print(str_end.format(sentence))

else:
    str_end = 'Wrong Input, please try again!'
    print(str_end)
