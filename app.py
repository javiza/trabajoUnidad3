from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
# Activa el modo depuracion
app.debug = True

@app.route('/')
def index():
    return '<a href=/formulario> Ingresa al formulario </a>'


# def home():
# return render_template('index.html')


@app.route('/nosotros')
def nosotros():
    return "¡nosotros que hacemos!"


@app.route('/contact')
def contact():
    return "¡ponte en contacto!"


@app.route('/user/<username>')
def show_user_profile(username):
    return f'Perfil del usuario: {username}'


@app.route('/perfil')
def perfil():
    datos_persona = {
        'nombre': 'juan',
        'edad': 20,
        'intereses': ['Python', 'Desarrollo Web']
    }
    return render_template('perfil.html', persona=datos_persona)


def calcular_cuadrado(numero):
    return numero ** 2


def calcular_cubo(numero):
    return numero ** 3


@app.route('/calcular/<int:numero>')
def calcular(numero):
    cuadrado = calcular_cuadrado(numero)
    cubo = calcular_cubo(numero)
    return render_template('resultados.html', numero=numero, cuadrado=cuadrado, cubo=cubo)


# ruta que recibe un arra como parametro en la url
@app.route('/array/<int_list>')
def process_array(int_list):
    return f'Array recibido: {int_list}', 200


# ruta que recibe un array como datos de un formulario post
@app.route('/submit', methods=['GET', 'POST'])
def submit_array():
    if request.method == 'POST':
        array_data = request.form.get('array').split(',')
        return f'array recibido: {array_data}', 200
    else:
        return render_template('form.html')


# ruta que envia un array como respuesta json
@app.route('/get_array', methods=['GET'])
def get_array():
    example_array = [1, 2, 3, 4, 5, 6]
    return jsonify(array=example_array)


# para el formulario

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        # procesar los datos del formulario
        nombre = request.form['nombre']
        correo = request.form['correo']
        # realizar acciones con los datos
        return f'¡hola, {nombre}! Tu correo es {correo}.'
    return render_template('formulario.html')


if __name__ == '__main__':
    app.run()
