from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#Crear la primera tabla de la base de datos
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String, nullable = False)
    apellido = db.Column(db.String, nullable = False)
    correo = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String)

# Crear la tabla de formulario de startups
class Startup(db.Model):
    id_startup = db.Column(db.Integer, primary_key = True)
    nombre_empresa = db.Column(db.String)
    descripcion = db.Column(db.String)
    fundadores = db.Column(db.String)
    modelo_de_negocio = db.Column(db.String)
    producto_servicio = db.Column(db.String)
    mercado_competencia = db.Column(db.String)
    proyeccion_financiera = db.Column(db.String)
    necesidad_financiamiento = db.Column(db.String)
    direccion = db.Column(db.String)
    contacto_correo = db.Column(db.String)
    contacto_telefono = db.Column(db.String)
    feedback = db.relationship("Feedback")

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    feedback = db.Column(db.String)
    startup_id = db.Column(db.Integer, db.ForeignKey("startup.id_startup"), nullable = False)
