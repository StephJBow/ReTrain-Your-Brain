from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Import all models

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://steph:password@localhost:5432/treatment_project"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import *

from controllers.bookings_controller import bookings_blueprint
app.register_blueprint(bookings_blueprint)

from controllers.treatment_controller import treatment_blueprint
app.register_blueprint(treatment_blueprint)


@app.route("/")
def home():
    return render_template('index.jinja')


# Import and Register Controllers

# @app.route("/")
# def home():
#     return render_template("index.jinja", title="Hello World")
