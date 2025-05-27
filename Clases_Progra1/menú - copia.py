    #Menú
suma1 = 0
num1 = 50
cont1 = 1

suma2 = 0
num2 = 100
cont2 = 1

suma3 = 0
num3 = 70
cont3 = 1


cont4 = 50
seguir = 'S'
import random
while(seguir != 'N' and seguir != 'n'):
    print("")
    print("Tarea de ciclos en  python\nDigita el número de la opción que deseas ver primero")
    opc = int(input("1.Primer ejercicio\n2.Segundo ejercicio\n3.tercer ejercicio\n4.Cuarto ejercicio\n"))
    match(opc):
        case 1:
            for i in range(0,51):
                print(i)
            while(cont1<=num1):
                suma1 += cont1
                cont1 += 1
            print("la suma de los numeros del 1 al 50 es", suma1)
            seguir = str(input("Digite S si desea volver al menú\nDigite N si desea salir\n"))
        case 2:
            while(cont2<=num2):
                suma2 += cont2
                cont2 += 1
            print("la suma de los numeros del 1 al 100 es", suma2)
            print("")
            for m in range(1,101):
                if(m % 3 == 0 and m % 7 ==0):
                    print("Los multiplos del 3 y 7 que hay del 1 al 100 son: ",m)
            print("")
            for i in range(0,101, 3):
                if(i > 0):
                    print("Los multiplos de 3 son: ", i)
            print("")
            for j in range(0,101, 7):
                if(i > 0):
                    print("Los multiplos de 7 son: ", j)
                    
            seguir = str(input("Digite S si desea volver al menú\nDigite N si desea salir\n"))
        case 3:
            while(cont3<=num3):
                suma3 += cont3
                cont3 += 1
            print("la suma de los numeros del 1 al 70 es", suma3)
            for i in range(1,71):
                if(i % 2 == 0):
                    print("Los pares del 1 al 70 son: ",i)
            print("")
            for i in range(1,71):
                if(i % 2 != 0):
                    print("Los impares del 1 al 70 son: ",i)
            seguir = str(input("Digite S si desea volver al menú\nDigite N si desea salir\n"))
        case 4:
            for i in range(1, 51):
                print(i)
            print("")
            while cont4 > 0:
                print(cont4)
                cont4 -= 1
            
            seguir = str(input("Digite S si desea volver al menú\nDigite N si desea salir\n"))
    
            
              
