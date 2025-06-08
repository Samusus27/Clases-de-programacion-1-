from flask import Flask, render_template, request, redirect, url_for
import sistema_escolar

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/alumnos', methods=['GET'])
def alumnos():
    lista = sistema_escolar.consultar_alumnos()
    return render_template('alumnos.html', alumnos=lista)


@app.route('/agregar_alumno', methods=['POST'])
def agregar_alumno():
    nombre = request.form['nombre']
    cedula = request.form['cedula']
    curso = request.form['curso']
    nota = float(request.form['nota'])
    sistema_escolar.agregar_alumno(nombre, cedula, curso, nota)
    return redirect(url_for('alumnos'))


@app.route('/profesores', methods=['GET'])
def profesores():
    lista = sistema_escolar.consultar_profesores()
    return render_template('profesores.html', profesores=lista)


@app.route('/agregar_profesor', methods=['POST'])
def agregar_profesor():
    nombre = request.form['nombre']
    cedula = request.form['cedula']
    curso = request.form['curso']
    sistema_escolar.agregar_profesor(nombre, cedula, curso)
    return redirect(url_for('profesores'))


@app.route('/cursos', methods=['GET'])
def cursos():
    lista = sistema_escolar.consultar_cursos()
    return render_template('cursos.html', cursos=lista)


@app.route('/agregar_curso', methods=['POST'])
def agregar_curso():
    nombre = request.form['nombre']
    codigo = request.form['codigo']
    profesor = request.form['profesor']
    horario = request.form['horario']
    sistema_escolar.agregar_curso(nombre, codigo, profesor, horario)
    return redirect(url_for('cursos'))


if __name__ == '__main__':
    app.run(debug=True)
