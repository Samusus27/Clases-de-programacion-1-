h = 3500
sal_sem = h * 48
emp = {}
seguro = 0.1017

opc = None
seguir = "S"

while (seguir != 'n' and seguir != 'N'):
    print()
    print("Base de datos de los empleados de la empresa\nPresione el número de la opción que desea realizar")
    try:
        opc = int(input(
            "1) Ingresar datos de empleado\n2) Ver datos del empleado\n3) Ver salario del empleado con las deducciones\n"))
    except ValueError:
        print("Por favor,debes ingresar un número.")
        continue
    print()
    match(opc):
        case 1:
            for i in range(8):
                print(f"\nIngresando datos de los empleados {i + 1}:")
                nombre = input("Digita el nombre del empleado:\n")
                while True:
                    cedula = input("Digita el número de cédula:\n")
                    if cedula in emp:
                        print("¡Error! Ya existe un empleado con esta cédula.")
                    else:
                        break

                while True:
                    try:
                        horas = float(
                            input("Digita la cantidad de horas laboradas:\n"))
                        break
                    except ValueError:
                        print(
                            "Por favor ingresa las horas trabajadas en números")

                empleado = {'nombre': nombre, 'horas': horas}
                emp[cedula] = empleado
            seguir = str(
                input("Digite S si desea volver al menú\nDigite N si desea salir\n"))

        case 2:
            buscar = input("Digite el número de cédula del empleado\n")
            if buscar in emp:
                trabajador = emp[buscar]
                print("Nombre:", trabajador['nombre'])
                print("horas trabajadas: ", trabajador['horas'])
            else:
                print("No existen los datos que se están buscando")
            seguir = str(
                input("Digite S si desea volver al menú\nDigite N si desea salir\n"))
        case 3:
            buscar = input("Digite el numero de cedula del empleado\n")
            if buscar in emp:
                trabajador = emp[buscar]
                horas = trabajador['horas']
                nombre = trabajador['nombre']
                pago = horas * h
                ccss = (pago * seguro)
                total = pago - ccss
                if horas > 48:
                    extra = h * 1.5
                    hora_extra = horas - 48
                    pago_extra = hora_extra * extra
                    total1 = sal_sem + pago_extra
                    ccss_extra = (total1 * seguro)
                    total_final = total1 - ccss_extra
                    total_salext = sal_sem + pago_extra
                    print(nombre)
                    print("El salario bruto del empleado en esta semana es de: ", sal_sem,
                          "\nHoras extra: ", hora_extra, "=", pago_extra, "\nTotal: ", total_salext)
                    print("El salario neto del empleado esta semanada es de: ",
                          total1, "\nCCSS: ", ccss_extra, "\nTotal: ", total_final)
                    if hora_extra > 12:
                        print(
                            "La cantidad de horas extra máximas para una persona semanalmente es de 12 horas, no explotes laboralmente a tus empleados!!! Eso no es humano!!!")
                elif horas <= 48:
                    print(nombre)
                    print(
                        "El salario bruto del empleado en esta semana es de: ", pago)
                    print("El salario neto del empleado esta semanada es de: ",
                          pago, "\nCCSS: ", ccss, "\nTotal: ", total)
            else:
                print("No existen los datos que se están buscando")

            seguir = str(
                input("Digite S si desea volver al menú\nDigite N si desea salir\n"))
