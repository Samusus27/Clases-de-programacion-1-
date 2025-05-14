alumno = ["Esteban","Pamela","Adrian", "Kimberly","Daniel","Samuel"]

estudiante = input("Ingrese el nombre del estudiante")

encuentra = estudiante in alumno

if(encuentra):
    print("El alumno ya existe")
else:
    print("Se procede a ingresesar al estudiante")
    alumno.append(estudiante)
    print("El estudiante",estudiante,"se agrego correctamente")

print(alumno)
