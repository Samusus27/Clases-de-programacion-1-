tupla = (4,"Hola",6,[1,2,3],6,350)

print(tupla)
print("El numero 4 esta dentro de la tupla ",4 in tupla)
print("Cual es la posicion de la palabra hola ",tupla.index("Hola"))
print("Cuantas veces esta repetido el numero 6 ",tupla.count(6))
print("El tamaño de la tupla es de ",len(tupla))
#convertir tupla en una lista
lista = list(tupla)
print(lista)
