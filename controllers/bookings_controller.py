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
    treatment_id = request.form['treatment_id']
    booking_date = request.form['booking_date']
    booking_time = request.form['booking_time']
    new_booking = Bookings(customer_name=customer_name, treatment_id = treatment_id, booking_date = booking_date, booking_time=booking_time)
    db.session.add(new_booking)
    db.session.commit()
    return redirect('/booking')

@bookings_blueprint.route('/booking/<id>/edit_booking')
def edit_booking_page(id):
    booking = Bookings.query.get(int(id))
    treatments = Treatments.query.all()
    return render_template('booking/edit_booking.jinja', booking=booking, treatments=treatments)

@bookings_blueprint.route('/booking/<id>/edit_booking', methods=['POST'])
def edit_booking(id):
    booking = Bookings.query.get(int(id))
    customer_name = request.form['customer_name']
    treatment_id = request.form['treatment_id']
    booking_date = request.form['booking_date']
    booking_time = request.form['booking_time']
    booking.customer_name=customer_name
    booking.treatment_id=treatment_id
    booking.booking_date=booking_date
    booking.booking_time=booking_time
    db.session.commit()   
    return redirect('/booking')

@bookings_blueprint.route('/booking/<id>/delete', methods=['POST'])
def delete_booking(id):
    booking=Bookings.query.get(int(id))
    db.session.delete(booking)
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