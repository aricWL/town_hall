from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
#from project.forms import
from project.models import Representative, TownHall, Question
from project.townhall.forms import RepForm
from project import db


townhall_blueprint = Blueprint(
    'townhall',
    __name__,
    template_folder = "templates"
)

@townhall_blueprint.route('/home')
def home():
	return render_template('townhall/home.html')

@townhall_blueprint.route('/citizen')
def citizen():
	return render_template('townhall/citizen.html')

@townhall_blueprint.route('new', methods=['POST', 'GET'])
def new():
	form = RepForm()
	return render_template('townhall/new.html', form=form)
