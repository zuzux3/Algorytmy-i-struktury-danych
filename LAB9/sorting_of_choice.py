def make_array(array_len):
    arrInFunc = []

    for a in range(array_len):
        arrInFunc.append(float (input()))

    return arrInFunc

def choice(array_in_function, size_of_array):
    while size_of_array > 0:
        min = array_in_function[0]
        k = 0
        for i in range (size_of_array):
            if arr[i] > min:
                min = arr[i]
                k = i
        
        bufor = array_in_function[size_of_array - 1]
        array_in_function[size_of_array - 1] = min
        array_in_function[k] = bufor
        size_of_array -= 1

    return array_in_function
