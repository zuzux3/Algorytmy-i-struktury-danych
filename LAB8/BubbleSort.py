def make_list(array_size):
    arr_in_func = []

    for a in range (array_size):
        arr_in_func.append(float (input ()))
    
    return arr_in_func

def bubbles(array_in_function, size_of_array):
    for i in range (size_of_array - 1):
        for j in range(0, size_of_array - i - 1):
            if array_in_function[j] > array_in_function[j + 1]:
                array_in_function[j], array_in_function[j + 1] = array_in_function[j + 1], array_in_function[j]
                
    return array_in_function
