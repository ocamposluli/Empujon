from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy # Importamos la libreria de la base de datos

db = SQLAlchemy() # Instanciamos la base de datos
app = Flask(__name__) # Instanciamos la app flask

# configurar la base de datos SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

# inicializar la app de la extension
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    usuario = db.Column(db.String, unique = True, nullable= False)
    password = db.Column(db.String)

@app.route("/")
def homepage():
    return render_template ("index.html")