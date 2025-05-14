import random
seguir = "S"
temp = []
opc = None

while (seguir != 'n' and seguir != 'N'):
    print()
    print("Estación metereológica\n \nDigita el número correspondiente a la opción que necesitas: \n ")
    opc = int(input("1) Rellenar lista de forma manual.\n2) Rellenar lista de forma aleatoria\n3) Mostrar datos\n4) Obtener datos máximos y mínimos\n5) Orden ascendente del componen\n6) Orden descendente del componente\n7) Salir\n"))
    print()
    match(opc):
        case 1:
            temp.clear()
            while len(temp) < 15:
                num = int(
                    input("Introduce las temperaturas de cada hora durante el día: "))
                if num <= 40:
                    temp.append(num)
                else:
                    print("La temperatura ingresada no puede pasar los 40°")
            print("Los datos fueron almacenados correctamente")

            seguir = str(
                input("Digite S si desea volver al menú\nDigite N si desea salir\n"))
        case 2:
            temp.clear()
            for i in range(15):
                elemento = random.randint(0, 40)
                temp.insert(i, elemento)

            print("Los datos fueron almacenados correctamente")
            seguir = str(
                input("Digite S si desea volver al menú\nDigite N si desea salir\n"))
        case 3:
            print(
                "Las temperaturas en Grados centígrados recolectadas cada hora fueron: \n")
            for t in temp:
                print(f"{t}°")

            seguir = str(
                input("Digite S si desea volver al menú\nDigite N si desea salir\n"))
        case 4:
            print(
                "La temperatura mal alta alcanzada el dia de hoy fueron:\n", max(temp), "°")
            print(
                "La temperatura mas baja alcanzada el dia de hoy fueron:\n", min(temp), "°")
            seguir = str(
                input("Digite S si desea volver al menú\nDigite N si desea salir\n"))

        case 5:
            temp.sort()
            print("Las temperaturas ordenadas de la más baja a la mas alta son: ")
            for t in temp:
                print(f"{t}°")
            seguir = str(
                input("Digite S si desea volver al menú\nDigite N si desea salir\n"))
        case 6:
            temp.reverse()
            print("Las temperaturas ordenadas de la más alta a la mas baja son: ")
            for t in temp:
                print(f"{t}°")
            seguir = str(
                input("Digite S si desea volver al menú\nDigite N si desea salir\n"))
        case 7:
            print("Programa terminado!!")
            break

    print()
