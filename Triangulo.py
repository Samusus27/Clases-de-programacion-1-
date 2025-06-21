##Solicitarle al usuario 3 datos que serán las dimensiones de un triángulo el sistema determinara el tipo de triángulo de acuerdo a lo siguiente:  
##si se cumple el teorema de Pitágoras es rectángulo,  
##si todos sus lados son iguales es equilátero,  
##si dos lados son iguales es isósceles en caso contrario es escaleno.  

lado1 = float(input("Digite la medida del primer lado o cateto: "))
lado2 = float(input("Digite la medida del segundo lado o cateto: "))
lado3 = float(input("Digite la medida del tercer lado o el lado mas largo: "))

if(lado3 ** 2 == lado1 ** 2 + lado2 ** 2):
    print("Es un triángulo rectangulo")
elif(lado1 == lado2 == lado3):
    print("Es un triágulo equilatero")
elif(lado1 == lado2 != lado3 or lado1 == lado3 !=lado2 or lado2 == lado3 != lado1):
    print("Es un triángulo isóceles")
else:
    print("Es un triángulo escaleno")

    
