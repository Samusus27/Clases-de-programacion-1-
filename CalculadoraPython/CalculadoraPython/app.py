from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def formulario():
    resultado = ''
    valor1 = ''
    operacion = ''
    if request.method == 'POST':
        resultado = request.form.get('resultado', '')
        valor1 = request.form.get('valor1', '')
        operacion = request.form.get('operacion', '')

        if 'n1' in request.form:
            resultado += '1'
        elif 'n2' in request.form:
            resultado += '2'
        elif 'n3' in request.form:
            resultado += '3'
        elif 'n4' in request.form:
            resultado += '4'
        elif 'n5' in request.form:
            resultado += '5'
        elif 'n6' in request.form:
            resultado += '6'
        elif 'n7' in request.form:
            resultado += '7'
        elif 'n8' in request.form:
            resultado += '8'
        elif 'n9' in request.form:
            resultado += '9'
        elif 'n0' in request.form:
            resultado += '0'

        elif 'nclear' in request.form:
            resultado = ''
            valor1 = ''
            operacion = ''
        elif 'nmas' in request.form:
            valor1 = resultado
            resultado = ''
            operacion = '+'
        elif 'nmenos' in request.form:
            valor1 = resultado
            resultado = ''
            operacion = '-'
        elif 'ndiv' in request.form:
            valor1 = resultado
            resultado = ''
            operacion = '÷'
        elif "nraiz" in request.form:
            valor1 = resultado
            resultado = ''
            operacion = '√'
        elif "ncuadrado" in request.form:
            valor1 = resultado
            resultado = ''
            operacion = 'x²'
        elif "nmulti" in request.form:
            valor1 = resultado
            resultado = ''
            operacion = 'x'

        elif 'nigual' in request.form:
            if operacion == '+' and valor1 != '':
                try:
                    total = int(valor1) + int(resultado)
                    resultado = str(total)
                    valor1 = ''
                    operacion = ''
                except:
                    resultado = 'Error'
            elif operacion == '-' and valor1 != '':
                try:
                    total = int(valor1) - int(resultado)
                    resultado = str(total)
                    valor1 = ''
                    operacion = ''
                except:
                    resultado = 'Error'
            elif operacion == 'x' and valor1 != '':
                try:
                    total = int(valor1) * int(resultado)
                    resultado = str(total)
                    valor1 = ''
                    operacion = ''
                except:
                    resultado = 'Error'
            elif operacion == '÷' and valor1 != '':
                try:
                    total = int(valor1) / int(resultado)
                    resultado = str(total)
                    valor1 = ''
                    operacion = ''
                except:
                    resultado = 'Error'
            elif operacion == '√' and valor1 != '':
                try:
                    total = int(valor1) ** 0.50
                    resultado = str(total)
                    valor1 = ''
                    operacion = ''
                except:
                    resultado = 'Error'
            elif operacion == 'x²' and valor1 != '':
                try:
                    total = int(valor1) ** 2
                    resultado = str(total)
                    valor1 = ''
                    operacion = ''
                except:
                    resultado = 'Error'

    return render_template('inicio.html', resultado=resultado, valor1=valor1, operacion=operacion)


if __name__ == '__main__':
    app.run(debug=True)
