import random

listA = []
listB = []
listC = []
suma = 0
cont = 0
#Crear Tres listas con números aleatorios de 10 campos las listas se llamarán listA (5,30), listB (10,20), listC (20,50)
for i in range(10):
    elemento1 = random.randint(5,30)
    listA.insert(i,elemento1)
print()
print("La lista A es\n",listA)
    

for j in range(10):
    elemento2 = random.randint(10,20)
    listB.insert(j,elemento2)
print()
print("La lista B es\n",listB)
    
for k in range(10):
    elemento3 = random.randint(20,50)
    listC.insert(k,elemento3)
print()
print("La lista C es:\n",listC)

#Utilizando las listas genere tres sublistas.
print()
print("Sublista de la lista A: ",listA[3:9])

print()
print("Sublista de la lista B: ",listA[2:11])

print()
print("Sublista de la lista C: ",listA[7:10])

#Saque el elemento menor y mayor de cada lista

print()
print("El elemento mayor de la lista A es: ",max(listA),"\nEl numero menor de la lista A es: ",min(listA))

print()
print("El elemento mayor de la lista B es: ",max(listB),"\nEl numero menor de la lista A es: ",min(listB))

print()
print("El elemento mayor de la lista C es: ",max(listC),"\nEl numero menor de la lista A es: ",min(listC))

#Saque la sumatoria de cada lista

print()
print("La sumatoria de la lista A es: ",sum(listA))

print()
print("La sumatoria de la lista B es: ",sum(listB))

print()
print("La sumatoria de la lista C es: ",sum(listC))

#Crear la listD basada en la listA con la listC

listD = listA + listC
print()
print("La lista D estaria basada en la lista A y C\ny sus números serian:\n",listD)

#Crear la listE basada en la listB con la listC

listE = listB + listC
print()
print("La lista E estaria basada en la lista B y C\ny sus números serian:\n",listE)

#Crear la listF basada en las tres 

listF = listA + listB + listC

print()
print("La lista F estaria basada en la lista A, B y C\ny sus números serian:\n",listF)

#Ingrese el elemento 31 al final de la listA, el elemento 25 al final de la listB y el 51 al final de la listC, debe verificar que el número no exista para poder ser ingresado

print()
if(31 in listA):
    print("No puede ser ingresado el 31 por que ya se encuentra en la lista A")
else:
    listA.append(31)
    print("Lista A ahora con el 31 agregado seria:",listA)

print()
if(25 in listB):
    print("No puede ser ingresado el 25 por que ya se encuentra en la lista B")
else:
    listB.append(25)
    print("Lista B ahora con el 25 agregado seria:",listB)

print()
if(51 in listC):
    print("No puede ser ingresado el 51 por que ya se encuentra en la lista C")
else:
    listC.append(51)
    print("Lista C ahora con el 51 agregado seria:",listC)

#Inserte los elementos 35 en la posición 2 de la listA, 21 en la posición 3 de la listB, 65 en la posición 1 de la listC

print()
listA.insert(1,35)
print("El numero 35 se agregó a la segunda posición y la lista A ahora sería:\n",listA)

print()
listB.insert(2,21)
print("El numero 21 se agregó a la tercera posición y la lista B ahora sería:\n",listB)

print()
listC.insert(0,65)
print("El numero 65 se agregó a la primera posición y la lista C ahora sería:\n",listC)

#Ordene de menor a mayor las listA, listB, listC

print()
listA.sort()
listB.sort()
listC.sort()
print("La lista A ordenada de menor a mayor seria:\n",listA)
print()
print("La lista B ordenada de menor a mayor seria:\n",listB)
print()
print("La lista C ordenada de menor a mayor seria:\n",listC)

#Imprimir de atrás hacia adelante las listas listE, listF, listD

print()
listD.sort()
listE.sort()
listF.sort()

listD.reverse()
listE.reverse()
listF.reverse()

print("La lista D ordenada de mayor a menor seria:\n",listD)
print()
print("La lista E ordenada de mayor a menor seria:\n",listE)
print()
print("La lista F ordenada de mayor a menor seria:\n",listF)
print()

#Imprimir de la listA los números pares.
listA.sort()
if (elemento1 % 2 == 0):
    print("Los números pares de la lista A son:\n",listA)
else:
    print("Ningún número de la lista A es par")





























