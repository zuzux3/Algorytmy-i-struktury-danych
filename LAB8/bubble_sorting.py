import BubbleSort

size_arr = int (input ("Podaj rozmiar listy, ktora chcesz posegregowac: "))

if size_arr > 1:
    arr = []
    order = 'Teraz podaj numery, ktore chcesz dodac do segregowanej listy: '
    result = 'Posegregowana lista = {}'
    
    print (order)

    arr = BubbleSort.make_list(size_arr)
    arr = BubbleSort.bubbles(arr, size_arr)

    print (result.format(arr))
    
else:
    print('Wrong input!\n')
