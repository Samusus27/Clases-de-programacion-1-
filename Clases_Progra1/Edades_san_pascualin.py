sistema_escolar = []
seguir = "S"
opc = None

while (seguir != 'n' and seguir != 'N'):
    print()
    print("Datos de las edades de los sistema_escolar de la escuala San Pascualín\nDigita el número correspondiente a la opción que deseas ver")
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
                        edad = int(
                            input("Digita la edad de los sistema_escolar "))
                        if 6 <= edad <= 14:
                            sistema_escolar.append(edad)
                            break
                        else:
                            print(
                                "\nLas edades de los sistema_escolar deben ser entre los 6 y 14 años")

            except ValueError:
                print("\nDigita la edad de los sistema_escolar en números")
                seguir = str(
                    input("\nDigite S si desea volver al menú\nDigite N si desea salir\n"))

        case 2:
            print("\nLas edades de los sistema_escolar son:\n", sistema_escolar)
            seguir = str(
                input("\nDigite S si desea volver al menú\nDigite N si desea salir\n"))
        case 3:
            sistema_escolar.sort()
            print(
                "\nLas edades de los sistema_escolar ordenadas de mayor a menor seria:\n", sistema_escolar)
            seguir = str(
                input("\nDigite S si desea volver al menú\nDigite N si desea salir\n"))
        case 4:
            print("\nLa suma de todas las edades se: \n", sum(sistema_escolar))
            seguir = str(
                input("\nDigite S si desea volver al menú\nDigite N si desea salir\n"))
        case 5:
            suma = sum(sistema_escolar)
            promedio = suma / len(sistema_escolar)
            print(
                "\nEl promedio de la lista de edades de los sistema_escolar es: \n", promedio)
            seguir = str(
                input("\nDigite S si desea volver al menú\nDigite N si desea salir\n"))
        case 6:
            print("\nLa lista actualmente es: ", sistema_escolar)
            print(
                "Los indices de cada edad:  0 - 1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10 ")
            edad = input("Ingrese la nueva edad que desea colocar: ")
            ind = int(
                input("Ingrese el indice(el lugar que va a ocupar la nueva edad en la lista) donde desea modificar el elemento: "))
            longitud = len(sistema_escolar)
            try:
                sistema_escolar[ind] = edad
                print("Elemento modifica!!")
            except IndexError:
                print("El indice debe de estar entre 0 y ", longitud)
            seguir = str(
                input("\nDigite S si desea volver al menú\nDigite N si desea salir\n"))
        case 7:
            print("La lista actualmente es: ", sistema_escolar)
            print(
                "Los indices de cada edad:  0- 1- 2- 3- 4- 5- 6- 7- 8- 9 ")
            ind = int(
                input("Ingrese el indice del elemento que desea eliminar: "))
            longitud = len(sistema_escolar)
            try:
                sistema_escolar.remove(edad)
                print("Elemento eliminado!!")
            except IndexError:
                print("El indice debe de estar entre 0 y ", longitud)
            seguir = str(
                input("\nDigite S si desea volver al menú\nDigite N si desea salir\n"))
        case 8:
            sistema_escolar.sort()
            print(sistema_escolar)
            longitud = len(sistema_escolar)
            if longitud % 2 != 0:
                mediana_impar = sistema_escolar[longitud // 2]
                print("La mediana de la lista de sistema_escolar es: ", mediana_impar)
            else:
                mediana_par = (sistema_escolar[longitud // 2 - 1] +
                               sistema_escolar[longitud // 2]) / 2
                print("La mediana de la lista de sistema_escolar es: ", mediana_par)
            seguir = str(
                input("\nDigite S si desea volver al menú\nDigite N si desea salir\n"))
