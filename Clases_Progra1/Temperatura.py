##Lea un valor de temperatura t y un código p que puede ser 1 o 2.
##Si el código es 1 convierta la temperatura t de grados c con la formula c= 5/9(t-32),
##en caso contrario convierta la temperatura t de grados a f con la formula f=32+9t/5.

t = float(input("Digite la temperatura: "))
print("1\n2")
opc = int(input("Digite uno de los siguientes números acontinuación: "))


match(opc):
    case 1:
        c= 5/9*(t-32)
        print("La temperatura en celcius es: ",c)
    case 2:
        f=32+9*t/5
        print("La temperatura en fahrenheit es: ",f)
        
