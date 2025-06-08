alumnos = []
profes = []
cursos = []


def agregar_alumno(nombre, cedula, curso, nota):
    for c in cursos:
        if c['nombre'].lower() == curso.lower():
            if c['inscritos'] >= c['capacidad']:
                print("⚠️ No hay cupo disponible en este curso.")
                return
            alumno = {
                'nombre': nombre,
                'cedula': cedula,
                'curso': curso,
                'nota': [float(nota)]
            }
            alumnos.append(alumno)
            c['inscritos'] += 1
            return
        incrementar_inscritos(curso)
    print("Curso no encontrado.")


def agregar_profesor(nombre, cedula, curso):
    profe = {
        'nombre': nombre,
        'cedula': cedula,
        'curso': curso
    }
    profes.append(profe)

    if not curso_existe(curso):
        codigo = "C-" + curso[:3].upper() + cedula[-3:]
        agregar_curso(nombre_curso=curso, codigo=codigo, profesor=cedula)


def agregar_curso(nombre_curso, codigo, profesor, horario='Por asignar', capacidad=30):
    for curso in cursos:
        if curso['nombre'].lower() == nombre_curso.lower():
            curso['horario'] = horario
            return
    clase = {
        'nombre': nombre_curso,
        'codigo': codigo,
        'profesor': profesor,
        'horario': horario,
        'capacidad': capacidad,
        'inscritos': 0,
        'Alumnos': [],
        'notas': []
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


def incrementar_inscritos(nombre_curso):
    for curso in cursos:
        if curso['nombre'].lower() == nombre_curso.lower():
            if 'inscritos' in curso:
                curso['inscritos'] += 1
            else:
                curso['inscritos'] = 1
