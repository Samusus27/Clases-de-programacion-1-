import alumnos
seguir = 's'


def menu():
    seguir = 's'
    while seguir.lower() != 'n':
        print("\nsistema escolar")
        print("1.Agregar\Consultar Alumnos")
        print("2.Agregar\Consultar Profesores")
        print("3.Agregar\Consultar Cursos")
        print("4.Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            subopcion = input(
                "a) Agregar Alumno\nb) Consultar Alumnos\nseleccione una opcion\n").lower()
            if subopcion == 'a':
                nombre = input("Nombre del alumno: ")
                cedula = input("Cedula del alumno: ")
                if not alumnos.consultar_cursos():
                    print("No hay cursos disponibles")
                    continue
                else:
                    print("Cursos disponibles: ", alumnos.consultar_cursos())
                curso = input("Curso del alumno: ")
                if not alumnos.curso_existe(curso):
                    print(
                        "El curso", curso, "no está registrado,\nPor favor agregalo primero en el apartado de cursos")
                    continue
                nota = float(input("Nota del alumno: "))
                alumnos.agregar_alumno(nombre, cedula, curso, nota)
            elif subopcion == 'b':
                for a in alumnos.consultar_alumnos():
                    print(a)
                print("El total de alumnos registrados es:",
                      alumnos.contar_alumnos())
                print("\nEl promedio de las notas de todos lo alumnos es: ",
                      alumnos.promedio_general())

                resultado = alumnos.resumen_resultados()
                print("La cantidad de alumnos que aprovaron es de: ",
                      resultado['aprobados'])
                print("La cantidad de alumnos aplazados es de: ",
                      resultado['aplazados'])
                print("La cantidad de alumnos que reprobaron es de: ",
                      resultado['reprobados'])

                mejoresP = alumnos.mejores_promedios()
                print("La cantidad de alumnos eximidos es de: ",
                      mejoresP['eximidos'])

            seguir = str(input("¿Desea seleccionar otra opción?  S/N"))

        if opcion == '2':
            subopcion = input(
                "a) Agregar Profesor\nb) Consultar Profesores\nseleccione una opcion\n").lower()
            if subopcion == 'a':
                nombre = input("Nombre del profesor: ")
                cedula = input("Cedula del profesor: ")
                curso = input("Curso del profesor: ")
                alumnos.agregar_profesor(nombre, cedula, curso)
            elif subopcion == 'b':
                for a in alumnos.consultar_profesores():
                    print(a)

            seguir = str(input("¿Desea seleccionar otra opción?  S/N"))

        if opcion == '3':
            subopcion = input(
                "a) Agregar Curso\nb) Consultar Cursos\nseleccione una opcion\n").lower()
            if subopcion == 'a':
                nombre = input("Nombre del Curso: ")
                codigo = input("Código del curso: ")
                alumnos.agregar_cursos(nombre, codigo)
            elif subopcion == 'b':
                for a in alumnos.consultar_cursos():
                    print(a)

            seguir = str(input("¿Desea seleccionar otra opción?  S/N"))


if __name__ == "__main__":
    menu()
