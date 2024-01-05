from flask import Flask, render_template, redirect, Blueprint, request
from app import db
from models import *

review_blueprint = Blueprint("testimonials", __name__)

@review_blueprint.route('/testimonials')
def review_page():
    testimonials = Testimonials.query.all()
    return render_template('testimonials/index.jinja', testimonials=testimonials)

@review_blueprint.route('/testimonials', methods=['POST'])
def leave_review():
    reviewer_name = request.form['reviewer_name']
    comment = request.form['comment']
    new_review = Testimonials(reviewer_name=reviewer_name, comment=comment)
    db.session.add(new_review)
    db.session.commit()
    return redirect('/')