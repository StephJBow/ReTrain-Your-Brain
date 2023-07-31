from flask import render_template, redirect, Blueprint, request
from app import app, db
from models import *
# Import models

treatment_blueprint = Blueprint('treatment', __name__)

@treatment_blueprint.route('/treatments')
def treatment_list():
    treatments = Treatments.query.all()
    return render_template('treatments/index.jinja', treatments=treatments)

# Example of showing an individual object
# @example_blueprint.route("/example/<id>")
# def example_show(id):
#     example_obj = Example.query.get(id)
#     return render_template("example/show.html", example=example_obj)