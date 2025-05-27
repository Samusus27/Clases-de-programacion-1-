#Pedir al usuario un valor. Si el valor es positivo,
#pedir un segundo valor y calcular la suma, resta y producto de ambos. Mostrar los resultados por pantalla. (operacion1)

num = int(input("Digita un número "))
if (num >= 0):
    num2 = int(input("Digita otro número "))
    suma = num + num2
    resta = num - num2
    multi = num * num2

    print("El resultado de la suma de los números es: ",suma,"\nEl resultado de la resta es:",resta,"\nEl resultado del producto es: ",multi)

else:
    print("El número no es válido")
    


