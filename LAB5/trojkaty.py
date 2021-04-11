a = float( input("Podaj dlugosc boku a: "))
b = float( input("Podaj dlugosc boku b: "))
c = float( input("Podaj dlugosc boku c: "))

if (a > 0 and b > 0 and c > 0):
    if ((a + b > c) and (a + c > b) and (b + c > a)):
        alfa = float( input("Podaj miare katu alfa: "))
        beta = float( input("Podaj miare katu beta: "))
        gamma = float( input("Podaj miare katu gamma: "))

        if (alfa > 0 and beta > 0 and gamma > 0):
            if alfa + beta + gamma == 180:
                if (a**2 + b**2 < c**2) and (90 < alfa < 180 or 90 < beta < 180 or 90 < gamma < 180):
                    if a == b or a == c or b == c:
                        trojkat = "rozwartokatny rownoramienny"
                    
                    else:
                        trojkat = "rozwartokatny roznoboczny"
                
                elif (a**2 + b**2 > c**2) and (alfa < 90 and beta < 90 and gamma < 90):
                    if a == b:
                        if a == c:
                            trojkat = "rownoboczny"
                        
                        else:
                            trojkat = "rownoramienny"
                    
                    else:
                        if a == c or b == c or a == b:
                            trojkat = "rownoramienny ostrokatny"
                        
                        else:
                            trojkat = "roznoboczny ostrokatny"

                elif (a**2 + b**2 == c**2) and (alfa == 90 or beta == 90 or gamma == 90):
                    if a == b or a == c or b == c:
                        trojkat = "prostokatny rownoramienny"
                    
                    else:
                        trojkat = "prostokatny roznoboczny"
                
                else:
                     print("Nie mozna zbudowac trojkata\n")
                
                str1 = "Podany trojkat to {}!\n"
                print(str1.format(trojkat))

            else:
                 print("Nie mozna zbudowac trojkata\n")
        
        else:
             print("Nie mozna zbudowac trojkata\n")

    else:
        print("Nie mozna zbudowac trojkata\n")

else:
    print("Nie mozna zbudowac trojkata\n")
