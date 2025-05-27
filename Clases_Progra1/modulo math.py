import math

x = float(input("Digite un numero"))

print("El numero ",x, " redondeado es: ",round(x))
print("El numero ",x, " redondeado hacia arriba es: ",math.ceil(x))
print("El numero ",x, " redondeado hacia abajo es: ",math.floor(x))
print("El trundcado del numero ",x, " es: ",math.trunc(x))
print("El reciduo del numero ",x, " es: ",round(math.fmod(x,3),2))
print("El numero ",x, " elevado a la 2 es: ",math.pow(x,2))

