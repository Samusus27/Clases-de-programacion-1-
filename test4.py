

usuario = []
while True:
    print("Sistema de Rentas internas de Costa Rica")
    print("\n1. Ingrese los datos del usuario")
    print("\n2. Consulte los datos del usuario")
    print("\n3. Salir.")

    opcion = input("\nSelecione la transacción que desea realizar: ")

    match opcion:
        case '1':
            nombre = input("\nDigite el nombre del nuevo usuario:  ")
            edad = int(input("\nDigite la edad del nuevo usuario:  "))
            ingreso = float(
                input("\nIngrese el monto recibido mensualmente en dólares:  "))
            if ingreso > 2000 and edad > 17:
                print(f"Estimado usuario {nombre} usted debe tributar")
            elif ingreso < 500 and edad > 17:
                print(f"Estimado usario {nombre} usted no debe tributar")
            else:
                print("Estimado usuario, usted no es apto para tributar")
            usuario.append(
                {'nombre': nombre, 'edad': edad, 'ingreso': ingreso})

        case '2':
            for usuarios in usuario:
                print("Nombre:", usuarios['nombre'])
                print("Edad:", usuarios['edad'])
                print("Ingreso:", usuarios['ingreso'])
                if usuarios['edad'] > 17 and usuarios['ingreso'] > 2000:
                    print("Debe tributar")
                elif usuarios['edad'] > 17 and usuarios['ingreso'] < 500:
                    print("No debe tributar")
                else:
                    print("No debe tributar")
        case '3':
            print("\nSaliendo del sistema... ¡Gracias!")
            break

        case _:
            print("\nOpción no válida. Intente nuevamente.")
