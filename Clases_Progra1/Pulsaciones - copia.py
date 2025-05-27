#Calcular el número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio aeróbico;
#la fórmula que se aplica cuando si el sexo es femenino: númeropulsaciones = (220 - edad) / 10
#en caso contrario número pulsaciones = (210 - edad) / 10 debe solicitar la edad y el sexo (Pulsaciones)

edad = int(input("Digite su edad"))
sexo = str(input("Digite su sexo"))
pulM = (210 - edad) / 10
pulF = (220 - edad) / 10
if( sexo == "Femenino" or sexo == "femenino" or sexo == "FEMENINO"):
    print("La cantidad de pulsaciones que tienes por cada 10seg de aeróbicos es:",pulF)
else:
    print("La cantidad de pulsaciones que tienes por cada 10seg de aeróbicos es:",pulM)
