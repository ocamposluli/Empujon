from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy # Importamos la libreria de la base de datos 
from modelos import db, User, Startup, Feedback

app = Flask(__name__) # Instanciamos la app Flask 

# Configurar la base de datos SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la app con la extension 
db.init_app(app)

# Crear la ruta de acceso
@app.route("/")
def landing():
    return render_template("landing.html")

# Crear login
@app.route("/login", methods =["GET", "POST"])
def login():
    if request.method == "POST":
        correo = request.form['correo']
        password = request.form['password']
        user = User.query.filter_by(correo = correo).first()
        if user and user.password == password:
            # Inicio de sesion exitoso
            return redirect("/")
        else:
            # Credenciales invalidas 
            return "Credenciales invalidas. Intenta de nuevo"
    return render_template("login.html")

# Crear registro
@app.route("/register", methods =["GET", "POST"])
def register():
    if request.method == "POST":
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        contra = request.form['pass']
        user = User(nombre = nombre, apellido = apellido, correo = correo, password = contra)
        db.session.add(user)
        db.session.commit()
        return "El registro se completo correctamente"
    return render_template("registro.html")

# Crear formulario de registro de startups
@app.route("/register_startup", methods =["GET", "POST"])
def register_startup():
    if request.method == "POST":
        nombre_startup = request.form['startup']
        descripciones = request.form['descripcion']
        equipo_fundador = request.form['equipo']
        modelo_negocio = request.form['modelo']
        producto_servicio = request.form['productoservicio']
        mercado_competencia = request.form['mercadocompetencia']
        proyeccion_financiera = request.form['proyeccionfinanciera']
        necedidad_financiamiento = request.form['necedidaddefinanciamiento']
        correo = request.form['correo']
        telefono = request.form['telefono']
        direccion = request.form['direccion']
        startup = Startup(nombre_empresa = nombre_startup, descripcion = descripciones, fundadores = equipo_fundador, modelo_de_negocio = modelo_negocio, producto_servicio = producto_servicio, mercado_competencia = mercado_competencia, proyeccion_financiera = proyeccion_financiera, necesidad_financiamiento = necedidad_financiamiento, contacto_correo = correo, contacto_telefono = telefono, direccion = direccion)
        db.session.add(startup)
        db.session.commit()
        return "El registro del formulario se completo correctamente"
    return render_template("formulario.html")

# Editar id
@app.route("/editar/<id>", methods =["GET", "POST"])
def editar(id):
    if request.method == "POST":
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        correo = request.form['correo']
        contra = request.form['pass']
        user = User.query.filter_by(id=id).first()
        user.nombre = nombre
        user.apellido = apellido
        user.correo = correo
        user.password = contra
        db.session.commit()
    user = User.query.filter_by(id=id).first()
    return render_template("editarusuario.html", usuario = user)

# Eliminar un dato
@app.route("/eliminar/<id>", methods =["POST"])
def eliminar(id):
    user = User.query.filter_by(id=id).first()
    db.session.delete(user)
    db.session.commit()
    return "Se elimino con exito"

# Editar formulario filtrando por id
@app.route("/editarform/<id_startup>", methods =["GET", "POST"])
def editarform(id_startup):
    if request.method == "POST":
        nombrestartup = request.form['nombrestartup']
        descripcion = request.form['descripciondelastartup']
        fundador = request.form['equipofundador']
        modelo = request.form['modelodenegocio']
        prodservi = request.form['productoservicio']
        mercomp = request.form['mercadocompetencia']
        proyfinan = request.form['proyeccionfinanciera']
        necfinan = request.form['necesidadfinanciamiento']
        direc = request.form['direccion']
        correo = request.form['correo']
        telefono = request.form['telefono']
        user = Startup.query.filter_by(id_startup=id_startup).first()
        user.nombre_empresa = nombrestartup
        user.descripcion = descripcion
        user.fundadores = fundador
        user.modelo_de_negocio = modelo
        user.producto_servicio = prodservi
        user.mercado_competencia = mercomp
        user.proyeccion_financiera = proyfinan
        user.necedidad_financiamiento = necfinan
        user.direccion = direc
        user.contacto_correo = correo
        user.contacto_telefono = telefono 
        db.session.commit()
    user = Startup.query.filter_by(id_startup=id_startup).first()
    return render_template("editarform.html", usuario = user)

# Eliminar una Startup 
@app.route("/eliminando/<id_startup>", methods =["POST"])
def eliminando(id_startup):
    user = Startup.query.filter_by(id_startup=id_startup).first()
    db.session.delete(user)
    db.session.commit()
    return "Se elimino el formulario con exito"

@app.route("/info/<id>")
def info(id):
    startup = Startup.query.filter_by(id_startup = id).first()
    # Agregar lo demas faltantes
    return render_template("informaciones.html", datos = startup)

@app.route("/startups")
def startups():
    todo = Startup.query.all() # Se usa all para poder seleccionar todo y no filtrar como en el caso anterior
    return render_template("vista_inversor.html", startups = todo)

@app.route("/seleccionada/<id>")
def seleccionada(id):
    seleccion = Startup.query.filter_by(id_startup = id).first()
    return render_template("vistaseleccionada.html", datos = seleccion)

@app.route("/contactos/<id>")
def contactos(id):
    contacto = Startup.query.filter_by(id_startup = id).first()
    return render_template("contactos.html", datos = contacto)

@app.route("/feedbacks/<id>", methods = ["GET", "POST"])
def feedbacks(id):
    if request.method == "POST":
        feedbacks = request.form['feedbacks']
        add = Feedback(startup_id = id, feedback = feedbacks)
        db.session.add(add)
        db.session.commit()
    return render_template("feedbacks.html", id=id)

if __name__=="__main__":
    app.run(debug=True)