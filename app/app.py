from flask import Flask, render_template, redirect, request, url_for, flash, session
import mysql.connector 
from werkzeug.security import generate_password_hash, check_password_hash
import base64

# Crear instancia
app = Flask(__name__)
app.secret_key = '1016947815'

# Configurar la conexión
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="agenda2024"
)


cursor = db.cursor()

@app.route('/password/<contraencrip>')
def encriptarcontra(contraencrip):
    # generar un hash de la contraseña
    encriptar = generate_password_hash(contraencrip)
    valor = check_password_hash(encriptar, contraencrip)
    return valor

@app.route('/Registrar', methods=['GET', 'POST'])
def registrar_usuario():
    if request.method == 'POST':
        Nombres = request.form.get('nombre')
        Apellidos = request.form.get('apellido')
        email = request.form.get('email')
        Direccion = request.form.get('direccion')
        Telefono = request.form.get('telefono')
        Usuario = request.form.get('usuario')
        Contrasena = request.form.get('Contraseña')
        encriptado = generate_password_hash(Contrasena)
        rol = request.form.get('txtrol')

        cursor.execute("SELECT * FROM persona WHERE UsuarioPerso = %s OR EmailPerso = %s", (Usuario, email))
        existing_user = cursor.fetchone()

        if existing_user:
            flash('El usuario o correo ya están registrados')
            return render_template('registrar.html')
        else:
            cursor.execute("INSERT INTO persona (NombrePerso, ApellidoPerso, EmailPerso, DireccionPerso, TelefonoPerso, UsuarioPerso, ContraseñaPerso, Rol) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (Nombres, Apellidos, email, Direccion, Telefono, Usuario, encriptado, rol))
            db.commit()
            return render_template('registrar.html')

    else:
        return render_template("registrar.html") 

@app.route('/sesion', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('txtusuario')
        password = request.form.get('txtcontrasena')

        cursor.execute("SELECT UsuarioPerso, ContraseñaPerso, Rol FROM persona WHERE UsuarioPerso = %s", (username,))
        usuario = cursor.fetchone()

        if usuario and check_password_hash(usuario[1], password):
            session['usuario'] = usuario[0]
            session['Rol'] = usuario[2]

            if usuario[2] == 'Administrador':
                return redirect(url_for('lista'))
            else:
                return redirect(url_for('listar'))
        else:
            return render_template('formulario.html', mensaje="Nombre de usuario o contraseña incorrectos")

    return render_template('formulario.html', mensaje=None)
    

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

@app.route('/lista')  
def lista():
    cursor.execute('SELECT * FROM persona')
    usuarios = cursor.fetchall()
    return render_template('index.html', usuarios=usuarios)

   

@app.route('/editar/<int:idper>', methods=['POST', 'GET'])
def editar_usuario(idper):
    if request.method == 'POST':
        nombreper = request.form.get('nombreper')
        apellidoper = request.form.get('apellidoper')
        emailper = request.form.get('emailper')
        direccionper = request.form.get('direccionper')
        telefonoper = request.form.get('telefonoper')
        usuarioper = request.form.get('usuarioper')
        contraper = request.form.get('contraper')
        rol = request.form.get('rol')

        sql = "UPDATE persona SET NombrePerso=%s, ApellidoPerso=%s, EmailPerso=%s, DireccionPerso=%s, TelefonoPerso=%s, UsuarioPerso=%s, ContraseñaPerso=%s, Rol=%s WHERE IdPersona=%s"
        cursor.execute(sql, (nombreper, apellidoper, emailper, direccionper, telefonoper, usuarioper, contraper, rol, idper))
        db.commit()

        return redirect(url_for('lista'))
    else:
        cursor.execute('SELECT * FROM persona WHERE IdPersona=%s', (idper,))
        data = cursor.fetchall()

        return render_template('editar.html', personas=data[0])


@app.route("/eliminaru/<int:id>", methods=['GET'])
def eliminar_usuario(id):
    cursor.execute("DELETE FROM persona WHERE IdPersona=%s", (id,))
    db.commit()
    return redirect(url_for('lista'))

@app.route('/agregarcancion', methods=['GET', 'POST'])
def agregar_cancion():
    if request.method == 'POST':
        titulo = request.form.get('txttitulo')
        artista = request.form.get('txtartista')
        genero = request.form.get('txtgenero')
        duracion = request.form.get('txtduracion')
        precio = request.form.get('txtprecio')
        lanzamiento = request.form.get('txtlanzamiento')
        imagen = request.files['txtimagen'].read()

        cursor = db.cursor()
        cursor.execute("INSERT INTO canciones (TituloCancion, NombreArtistaCancion, Genero, Duracion, Precio, Lanzamiento, Img) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                       (titulo, artista, genero, duracion, precio, lanzamiento, imagen))
        db.commit()

        return redirect(url_for('listar_canciones'))  

    else:
        return render_template('Acancion.html')

@app.route('/actualizar/<int:id>', methods=['GET', 'POST'])
def editar_cancion(id):
    if request.method == 'POST':
        titulo = request.form.get('title')
        artista = request.form.get('artist')
        genero = request.form.get('genre')
        precio = request.form.get('precio')
        duracion = request.form.get('duration')
        lanzamiento = request.form.get('Fec_lan')

        sql = "UPDATE canciones SET TituloCancion=%s, NombreArtistaCancion=%s, Genero=%s, Precio=%s, Duracion=%s, Lanzamiento=%s WHERE IdCancion=%s"
        cursor.execute(sql, (titulo, artista, genero, precio, duracion, lanzamiento, id))
        db.commit()

        return redirect(url_for('listar_canciones'))
    else:
        cursor.execute('SELECT * FROM canciones WHERE IdCancion=%s', (id,))
        cancion = cursor.fetchone()

        if cancion:
            return render_template('actualizar.html', cancion=cancion)
        else:
            return render_template('actualizar.html')

@app.route("/eliminar/<int:id>", methods=['POST'])  # Cambiado a POST
def eliminar_cancion(id):
    if request.method == 'POST':  # Asegurarse de que solo se accede con POST
        cursor.execute('DELETE FROM canciones WHERE IdCancion = %s', (id,))
        db.commit()
        return redirect(url_for("listar_canciones"))
    else:
        return "Método no permitido"

@app.route('/listar')
def listar_canciones():
    cursor = db.cursor()
    cursor.execute("SELECT IdCancion, TituloCancion, NombreArtistaCancion, Genero, Precio, Duracion, Lanzamiento, Img FROM canciones")
    canciones = cursor.fetchall()

    if canciones:
        canciones_list = []
        for cancion in canciones:
            imagen = base64.b64encode(cancion[7]).decode('utf-8')
            canciones_list.append({
                'id': cancion[0],
                'titulo': cancion[1],
                'artista': cancion[2],
                'genero': cancion[3],
                'precio': cancion[4],
                'duracion': cancion[5],
                'lanzamiento': cancion[6],
                'imagen': imagen
            })

        return render_template('canciones.html', canciones=canciones_list)
    else:
        mensaje = "No hay canciones disponibles."
        return render_template('canciones.html', mensaje=mensaje)
    
@app.route('/agregar-al-carro', methods=['POST'])
def agregar_al_carrito():
    id_Can = request.form['IdCancion']
    titulocan = request.form['TituloCancion']
    preciocan = request.form['Precio']

    if 'cart' not in session:
        session['cart'] = []

    session['cart'].append({'id': id_Can, 'titulo': titulocan, 'precio': float(preciocan)})
    session.modified = True

    print("contenido del carro", session['cart'])

    return {'message': 'cancion agregada al carro'}


@app.route('/carritoo', methods=['GET', 'POST'])
def ver_carrito():
    carro = session.get('cart', [])
    total = sum(item['precio'] for item in carro)

    return render_template('carrito.html', carro=carro, total=total)

if __name__ == '__main__':
    app.run(debug=True, port=5005)
