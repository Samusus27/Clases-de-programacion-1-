##Calcule la potencia solicite la base y el exponente, de acuerdo a lo siguiente:
##si el exponente es positivo se calcula la potencia en caso contrario el resultado es un -1. 

base = int(input("Digite la base :"))
expo = int(input("Digite el exponente"))
potencia = base ** expo
if(expo > 0):
    print(base,"elevado a ",expo,"es",potencia)
else:
    print("El resultado es -1")
