from flask_login import UserMixin
from sqlalchemy import Numeric
from datetime import datetime
from app import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# ------------------- User Model -------------------
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(120), nullable=False)
    lastname = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    country = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    profile_image = db.Column(db.String(50), nullable=False, default="profile.png" ) 
    dob = db.Column(db.Date, nullable=True)
    
    password_hash = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(120), nullable=False)

    account_bal = db.Column(Numeric(12, 2), default=0.00)

    is_admin = db.Column(db.Boolean(), default=True)
    remember_me = db.Column(db.Boolean(), default=False)

    # Relationships
    investments = db.relationship("Investment", backref="user", lazy=True)
    transactions = db.relationship("Transaction", backref="user", lazy=True)

    def __repr__(self):
        return f"<User {self.id} - {self.firstname} {self.lastname}>"


# ------------------- Investment Type -------------------
class InvestmentType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)  
    description = db.Column(db.String(200), nullable=False, unique=False) 
    logo = db.Column(db.String(50), nullable=False, default="default.png" ) 
    investments = db.relationship('Investment', backref='investment_type', lazy=True)

# ------------------- Investment Model -------------------
class Investment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey("investment_type.id"), nullable=False)

    balance = db.Column(Numeric(12, 2), default=0.00)
    invested_amount = db.Column(Numeric(12, 2), default=0.00)
    percentage_increase = db.Column(Numeric(5, 2), default=0.00)
    percentage_decrease = db.Column(Numeric(5, 2), default=0.00)
    is_active = db.Column(db.Boolean(), default=False)


    type = db.relationship("InvestmentType")

    def __repr__(self):
        return f"<Investment {self.id} - {self.type.name} for User {self.user_id}>"


# ------------------- Transaction Model -------------------
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    investment_type_id = db.Column(db.Integer, db.ForeignKey("investment_type.id"), nullable=True)

    amount = db.Column(Numeric(12, 2), nullable=False)
    transaction_type = db.Column(db.String(50))  # 'profit', 'loss', 'deposit', etc.
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    investment_type = db.relationship("InvestmentType")

    def __repr__(self):
        return f"<Transaction {self.id} - {self.transaction_type} ${self.amount} for User {self.user_id}>"
