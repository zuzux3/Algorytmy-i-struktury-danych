def coding(text):
    key = 3
    fcode = ''

    for i in range(len (text)):
        if ( ord(text[i]) > 122 - key):
            if ord(text[i]) != 32:
                fcode += chr (ord(text[i]) + key - 26)
            else:
                fcode += ord(text[i])
        
        else:
            if ord(text[i]) != 32:
                fcode += chr (ord(text[i]) + key)
            else:
                fcode += chr (ord(text[i]))
    
    return fcode

def decoding(text):
    key = 3
    keym = key % 26
    fdecode = ''

    for i in range(len (text)):
        if (ord(text[i]) - keym < 97):
            if ord(text[i]) != 32:
                fdecode += chr ( ord(text[i]) - keym + 26)
            else:
                fdecode += chr (ord(text[i]))
           
        else:
            if ord(text[i]) != 32:
                fdecode += chr ( ord(text[i]) - keym)
            else:
                fdecode += chr (ord(text[i]))
    
    return fdecode
