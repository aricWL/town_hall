from flask import Flask, redirect
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CsrfProtect
import os

app = Flask(__name__, static_url_path='/static')
modus = Modus(app)
CsrfProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/boiler1_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "STRING"
app.config['TEMPLATES_AUTO_RELOAD'] = True

db = SQLAlchemy(app)


#from project.boiler1.views import boiler1_blueprint
#This is where you import more blueprints. Don't forget to register them below!


#app.register_blueprint(boiler1_blueprint, url_prefix='/boiler1')
#app.register_blueprint(boiler2_blueprint, url_prefix='/boiler1/<int:user_id>/boiler2')

@app.route('/')
def root():
    return redirect('/boiler1')