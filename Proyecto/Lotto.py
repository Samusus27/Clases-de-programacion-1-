import random

print("Bienvenido(a) al Loto tenemos muchos premios para vos")
print("tenemos premios desde los ₡100mil hasta los 5 millones de colones")
print()

nums = []

while len(nums) < 6:
    num = int(input("Introduce 6 números del 1 al 36 que tienes para el juego: "))
    if 1 <= num <= 36:
        if num not in nums:
            nums.append(num)
        else:
            print("El número elegido ya fue ingresado, por favor elige otro número")
    else:
        print("El número a elegir debe ser del 1 al 36")

print("Los numeros seleccionados son: \n", nums)

Lotto = []

for i in range(6):
    elemento = random.randint(1, 36)
    Lotto.insert(i, elemento)

print("La lista de numeros ganadores es: \n", Lotto)
comparar1 = set(Lotto)
comparar2 = set(nums)
aciertos = comparar1.intersection(comparar2)

print("Los aciertos que tuviste fueron: \n", aciertos)

if len(aciertos) == 6:
    print("Felicidades!!! Ganaste ₡5,000,000")
elif len(aciertos) == 5:
    print("Felicidades!!! Ganaste ₡1,000,000")
elif len(aciertos) == 4:
    print("Felicidades!!! Ganaste ₡500,000")
elif len(aciertos) == 3:
    print("Felicidades!!! Ganaste ₡100,000")
else:
    print("Lo siento, no has ganado el Lotto")


print()
