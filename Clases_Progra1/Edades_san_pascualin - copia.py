alumnos = []
seguir = "S"
opc = None

while (seguir != 'n' and seguir != 'N'):
    print()
    print("Datos de las edades de los alumnos de la escuala San Pascualín\nDigita el número correspondiente a la opción que deseas ver")
    try:
        opc = int(input("1) Almacenar las edades de los estudiantes.\n2) Mostrar lista.\n3) Obtener edad de mayor a menor.\n4) Calcular la suma de las edades.\n5) Calcular el promedio de las edades.\n6) Modificar una edad.\n7) Eliminar una edad.\n8) Calcular y mostrar la media de las edades."))
    except ValueError:
        print("Por favor,debes ingresar un número.")
        continue
    print()
    match(opc):
        case 1:
            try:
                for i in range(10):
                    while True:
                        edad = int(input("Digita la edad de los alumnos "))
                        if 6 <= edad <= 14:
                            alumnos.append(edad)
                            break
                        else:
                            print(
                                "\nLas edades de los alumnos deben ser entre los 6 y 14 años")

            except ValueError:
                print("\nDigita la edad de los alumnos en números")
                seguir = str(
                    input("\nDigite S si desea volver al menú\nDigite N si desea salir\n"))

        case 2:
            print("\nLas edades de los alumnos son:\n", alumnos)
            seguir = str(
                input("\nDigite S si desea volver al menú\nDigite N si desea salir\n"))
        case 3:
            alumnos.sort()
            print(
                "\nLas edades de los alumnos ordenadas de mayor a menor seria:\n", alumnos)
            seguir = str(
                input("\nDigite S si desea volver al menú\nDigite N si desea salir\n"))
        case 4:
            print("\nLa suma de todas las edades se: \n", sum(alumnos))
            seguir = str(
                input("\nDigite S si desea volver al menú\nDigite N si desea salir\n"))
        case 5:
            suma = sum(alumnos)
            promedio = suma / len(alumnos)
            print("\nEl promedio de la lista de edades de los alumnos es: \n", promedio)
            seguir = str(
                input("\nDigite S si desea volver al menú\nDigite N si desea salir\n"))
        case 6:
            print("\nLa lista actualmente es: ", alumnos)
            print(
                "Los indices de cada edad:  0 - 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10 ")
            edad = input("Ingrese la nueva edad que desea colocar: ")
            ind = int(
                input("Ingrese el indice(el lugar que va a ocupar la nueva edad en la lista) donde desea modificar el elemento: "))
            longitud = len(alumnos)
            try:
                alumnos[ind] = edad
                print("Elemento modifica!!")
            except IndexError:
                print("El indice debe de estar entre 0 y ", longitud)
            seguir = str(
                input("\nDigite S si desea volver al menú\nDigite N si desea salir\n"))
        case 7:
            print("La lista actualmente es: ", alumnos)
            print(
                "Los indices de cada edad:  0- 1- 2- 3- 4- 5- 6- 7- 8- 9 ")
            ind = int(
                input("Ingrese el indice del elemento que desea eliminar: "))
            longitud = len(alumnos)
            try:
                alumnos.remove(edad)
                print("Elemento eliminado!!")
            except IndexError:
                print("El indice debe de estar entre 0 y ", longitud)
            seguir = str(
                input("\nDigite S si desea volver al menú\nDigite N si desea salir\n"))
        case 8:
            alumnos.sort()
            print(alumnos)
            longitud = len(alumnos)
            if longitud % 2 != 0:
                mediana_impar = alumnos[longitud // 2]
                print("La mediana de la lista de alumnos es: ", mediana_impar)
            else:
                mediana_par = (alumnos[longitud // 2 - 1] +
                               alumnos[longitud // 2]) / 2
                print("La mediana de la lista de alumnos es: ", mediana_par)
            seguir = str(
                input("\nDigite S si desea volver al menú\nDigite N si desea salir\n"))
