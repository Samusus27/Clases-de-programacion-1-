alumnos = []
profes = []
cursos = []


def agregar_alumno(nombre, cedula, curso, nota):
    alumno = {
        'nombre': nombre,
        'cedula': cedula,
        'curso': curso,
        'nota': [float(nota)]
    }
    alumnos.append(alumno)


def agregar_profesor(nombre, cedula, curso):
    profe = {
        'nombre': nombre,
        'cedula': cedula,
        'curso': curso,
    }
    profes.append(profe)


def agregar_cursos(nombre, codigo):
    clase = {
        'nombre': nombre,
        'codigo': codigo,
    }
    cursos.append(clase)


def consultar_alumnos():
    return alumnos


def consultar_profesores():
    return profes


def consultar_cursos():
    return cursos


def curso_existe(nombre):
    return any(c['nombre'].lower() == nombre.lower() for c in consultar_cursos())


def contar_alumnos():
    return len(alumnos)


def promedio_general():
    total_notas = 0
    cantidad_notas = 0
    for alumno in alumnos:
        total_notas += sum(alumno['nota'])
        cantidad_notas += len(alumno['nota'])
    if cantidad_notas == 0:
        return 0
    return total_notas / cantidad_notas


def resumen_resultados():
    aprobados = 0
    aplazados = 0
    reprobados = 0

    for alumno in alumnos:
        if 'nota' in alumno and alumno['nota']:
            promedio = sum(alumno['nota']) / len(alumno['nota'])

            if promedio > 70:
                aprobados += 1
            elif promedio >= 60:
                aplazados += 1
            else:
                reprobados += 1

    return {
        'aprobados': aprobados,
        'aplazados': aplazados,
        'reprobados': reprobados
    }


def mejores_promedios():
    eximidos = 0
    for alumno in alumnos:
        if 'nota' in alumno and alumno['nota']:
            promedio = sum(alumno['nota']) / len(alumno['nota'])

            if promedio > 90:
                eximidos += 1

    return {
        'eximidos': eximidos
    }
