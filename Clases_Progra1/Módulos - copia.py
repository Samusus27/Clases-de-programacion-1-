## Si x, y, z valores x (3,9), y (20,30), z (15,25), determina el valor de las siguientes expresiones  
import math
import random
x = random.randint(3,9)
y = random.randint(20,30)
z = random.randint(15,25)

a = x + y + z
c = x / y
e = x / (y + z)
g = 2 * x / 3 * y
i =x * y % z
k = 3 * x - z - 2 * x
m = x - 100 % y % z

print("El resultado del ejercicio (a) es: ",math.sqrt(a))
print("El resultado del ejercicio (c) es: ",math.ceil(c))
print("El resultado del ejercicio (e) es: ",math.floor(e))
print("El resultado del ejercicio (g) es: ",math.trunc(g))
print("El resultado del ejercicio (i) es: ",i)
print("El resultado del ejercicio (k) es: ",k)
print("El resultado del ejercicio (m) es: ",m)
