from app import db, login_manager
from flask_login import UserMixin




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(120), nullable=False)
    lastname = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    country = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    dob = db.Column(db.Date, nullable=True)  # Allow null values
    is_admin = db.Column(db.Boolean(), default=False)
    remember_me = db.Column(db.Boolean(), default=False)

    def __repr__(self):
        return f"User_{self.id}('firstName-{self.firstname}', 'lastName-{self.lastname}', 'email-{self.email}', 'D.O.B-{self.dob}', 'phone-{self.phone}', 'country-{self.country}', 'state-{self.state}', 'address-{self.address}', 'password_hash-{self.password_hash}', 'is_admin-{self.is_admin}',)"


