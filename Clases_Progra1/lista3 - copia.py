a = [1,2,3,4,5,6,7,20]
b = [8,9,10,11,12,13,14,15]

print("Los elementos de la lista a son ")
print(a)
print("Los elementos de la lista b son ")
print(b)

c = a + b

print("Los elementos de la lista c son ")
print(c)
print("El tamanño de la lista es de ",len(c))
print("El numero mayor de la lista es ",max(c))
print("El numero menor de la lista es ",min(c))
print("La sumatoria de la lista es ",sum(c))
c.append(25)
c.insert(4,33)
print("Los elementos de la lista c son ")
print(c)
c.sort()
print("Los elementos de la lista c son ")
print(c)
c.reverse()
print("Los elementos de la lista c de atras hacia adelante son ")
print(c)
print("¿El número 12 está en la posición?",c.index(12))
print("¿Cuantas veces esta el numero 8 en la lista?",c.count(8))
