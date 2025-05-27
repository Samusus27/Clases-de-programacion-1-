import random
a = []
suma = 0
cont = 0

for i in range(10):
    elemento = random.randint(1,20)
    a.insert(i,elemento)
    if(elemento%2==0):
        cont+=1
        suma +=int(a[i])
print("Los elementos de la lista a son ")
print(a)
print("La sumatoria de los numeros pares es ",suma)
print("la cantidad de numeros pares son ",cont)
      
      
