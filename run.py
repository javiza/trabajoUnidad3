from flask import Flask, request, render_template

app = Flask(__name__)
# Activa el modo depuracion
app.debug = True


@app.route('/')
def index():
    return render_template('home.html')


# funcion para calcular

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    def promedio(nota1, nota2, nota3):
        suma = nota1 + nota2 + nota3
        promedio: float = suma / 3
        return promedio

    if request.method == 'POST':
        # tomando los datos desde el formulario
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])
        # proceso de los datos
        if nota1 < 10 and nota2 < 10 and nota3 < 10:
            return 'La nota debe ser mayor a 10'

        elif nota1 > 70 and nota2 > 70 and nota3 > 70:
            return 'la nota no debe ser mayor a 70'
        elif asistencia < 0 and asistencia > 100:
            return ' la asistencia debe ser entre el rango de 0 a 100'

        else:
            promedio = promedio(nota1, nota2, nota3)
            resultado = "APROBADO"
            if promedio >= 40 and asistencia > 75:
                return render_template('ejercicio1.html', resultado=resultado, promedio=promedio)
            else:
                return f'REPROBADO promedio: {promedio} Asistencia: {asistencia}'
    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        # tomando los datos desde el formulario y capturando el largo con len()
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        largo1 = len(nombre1)
        largo2 = len(nombre2)
        largo3 = len(nombre3)

        # proceso de los datos
        if largo1 > largo2 and largo1 > largo3:
            nombre = f'El nombre con mayor cantidad de caracteres es: {nombre1}'
            largo = f'el nombre tiene: {largo1} caracteres'
            return render_template('ejercicio2.html', nombre=nombre, largo=largo)

        elif largo2 > largo1 and largo2 > largo3:
            nombre = f'El nombre con mayor cantidad de caracteres es: {nombre2}'
            largo = f'el nombre tiene: {largo2} caracteres'
            return render_template('ejercicio2.html', nombre=nombre, largo=largo)

        elif largo3 > largo1 and largo3 > largo2:
            nombre = f'El nombre con mayor cantidad de caracteres es: {nombre3}'
            largo = f'el nombre tiene: {largo3} caracteres'
            return render_template('ejercicio2.html', nombre=nombre, largo=largo)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run()
