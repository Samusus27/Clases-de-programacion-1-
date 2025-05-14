#Solicitarle al usuario una nota, calcule su promedio (nota 1 + nota 2) /2 sabiendo que la segunda nota es el doble de la primera,
#debe indicar aprobado si el promedio es mayor o igual a 70.  (Notas)
import random
nota = int(input("Digite el resultado de su examen de Introducción a la programación: "))
nota2 = random.randint(0,100)
promedio = (nota + nota2) / 2

if( promedio >= 70 ):
    print("Su segunda calificación fue: ",nota2,"\nPor lo tanto su promedio es de: ",promedio,"\nAPROBADO")
else:
    print("Su segunda calificación fue: ",nota2,"\nPor lo tanto su promedio es de: ",promedio,"\nREPROBADO")
