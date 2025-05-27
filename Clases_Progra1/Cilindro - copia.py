#Dados el radio y la altura de un cilindro calcule la total área y el volumen de dicho cilindro. 
radio = float(input("Digite el radio del cilindro con decimales"))
altura = float(input("Digite la altura del cilindro con decimales"))
A = 2 * 3.141592653589793 * radio **2 + 2 * 3.141592653589793 * radio * altura
V = 3.141592653589793 * radio ** 2 * altura
print("La Area del cilindro es: ",A,"\nEl Volumen del cilindro es: ",V)
            
 #No sé porqué no me funcionó el math.pi
