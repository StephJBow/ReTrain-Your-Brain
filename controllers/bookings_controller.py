from flask import Flask, render_template, redirect, Blueprint, request
from app import db
from models import *

bookings_blueprint = Blueprint("booking", __name__)

@bookings_blueprint.route('/booking')
def bookings_list():
    bookings = Bookings.query.all()
    return render_template('booking/index.jinja', bookings_list=bookings)

# @bookings_blueprint.route("/booking/<id>")
# def show_booking(id):
#     booking = Bookings.query.get(id)
#     return render_template('booking/show.jinja', booking=booking)

@bookings_blueprint.route('/new_booking')
def new_booking_page():
    treatments = Treatments.query.all()
    bookings = Bookings.query.all()
    return render_template('/new_booking.jinja', treatments=treatments, bookings=bookings)

@bookings_blueprint.route('/new_booking', methods=['POST'])
def new_booking():
    customer_name = request.form['customer_name']
    treatment_name = request.form['treatment_name']
    booking_date = request.form['booking_date']
    booking_time = request.form['booking_time']
    new_booking = Bookings(customer_name=customer_name, treatment_name = treatment_name, booking_date = booking_date, booking_time=booking_time)
    db.session.add(new_booking)
    db.session.commit()
    return redirect('/booking')

@bookings_blueprint.route('/booking/<id>/edit')
def edit_booking_page(id):
    bookings = Bookings.query.get(int(id))
    return render_template('bookings/edit_booking.jinja', bookings=bookings) #create edit_booking.jinja

@bookings_blueprint.route('/booking/<id>/edit', methods=['POST'])
def edit_booking(id):
    bookings = Bookings.query.get(int(id))
    treatment_name = request.form['treatment_name']
    booking_date = request.form['booking_date']
    booking_time = request.form['booking_time']
    id = int(request.form['id'])
    bookings.treatment_name=treatment_name
    bookings.booking_date=booking_date
    bookings.booking_time=booking_time
    db.session.commit()   
    return redirect('/booking')

# @bookings_blueprint.route('/booking', methods=['POST'])
# def show_bookings():
#     id = int(request.form['id'])
#     booking_name = request.form['booking_name']
#     booking_date = request.form['booking_date']
#     booking_time = request.form['booking_time']
#     # treatment_id = db.Column(db.Integer, db.ForeignKey('treatments.id'))
#     show_bookings = Bookings(id = id, booking_name = booking_name, booking_date = booking_date, booking_time=booking_time)
    
#     db.session.add(show_bookings)
#     db.session.commit()

#     return redirect('/booking')



# Example of showing an individual object
# @example_blueprint.route("/example/<id>")
# def example_show(id):
#     example_obj = Example.query.get(id)
#     return render_template("example/show.html", example=example_obj)