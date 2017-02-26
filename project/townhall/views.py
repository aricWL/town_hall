from flask import Flask, render_template, request, redirect, url_for, flash, Blueprint
#from project.forms import
from project.models import Representative, TownHall, Question
from project import db


townhall_blueprint = Blueprint(
    'townhall',
    __name__,
    template_folder = "templates"
)