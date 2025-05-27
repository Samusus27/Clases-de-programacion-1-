import datetime

#funcion de procedimiento

def saludo():
    nombre = input("Digite su nombre ")
    print("Hola",nombre)

def calcular_edad(nac):
    fecha = datetime.datetime.now()#fecha actual del sistema 03/03/25 19:31
    date = fecha.date()# extrae solo la fecha 03/03/2025
    actual = int(date.strftime("%Y")) #funcion que extrae solo el año
    edad = actual - nac
    return edad

saludo()
nac = int(input("Digite el año de nacimiento "))
#today = calcular_edad() 
print("Su edad es",calcular_edad(nac))#aqui lo manda a llamar con today
    
