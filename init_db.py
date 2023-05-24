from modelos import db, User, Startup
from flask import Flask 

app = Flask("app")

# Configuracion de sqlalchemy 
# Configurar la base de datos SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializamos la base de datos 
db.init_app(app) # app es el servidor de Flask

# Creamos la base de datos
with app.app_context():
    db.create_all()
