from app import db

class Treatments(db.Model):
    __tablename__ = "treatments"

    id = db.Column(db.Integer, primary_key = True)
    treatment_name = db.Column(db.String(64))
    treatment_price = db.Column(db.String(64))
    treatment_length = db.Column(db.Integer)
    bookings = db.relationship('Bookings', backref='treatment', lazy=True)

    def __repr__(self):
        return f'<Treatments: {self.id} {self.treatment_name} {self.treatment_price} {self.treatment_length}>'


class Bookings(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key = True)
    customer_name = db.Column(db.String(64))
    booking_date = db.Column(db.String(64))
    booking_time = db.Column(db.String(64))
    treatment_id = db.Column(db.Integer, db.ForeignKey('treatments.id'))

    def __repr__(self):
        return f'<Bookings: {self.id}: {self.customer_name} {self.booking_date} {self.booking_time}>'


# Example Model
# ------------------------------------------------
# class User(db.Model):
#     __tablename__ = "users"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64))