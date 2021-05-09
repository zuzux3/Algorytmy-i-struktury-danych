from sorting_of_choice import make_array, choice

length = int (input ("Wprowadz wielkosc tablicy: "))

if length > 1:
    string1 = "Podaj wartosci tablicy:\n"
    string2 = "Posortowana tablica = {}\n"
    arr = []

    print(string1)
    arr = make_array(length)
    arr = choice(arr, length)

    print(string2.format(arr))

else:
    wrong = 'Wrong input!'
    print(wrong)
