from app import app
from flask import render_template
from flask_login import login_required, current_user
from app.models.user import User

@app.route('/dashboard')
@login_required
def dashboard():
    
    balance = "99,930"
    user = {
        "fname" : current_user.firstname,
        "lname" : current_user.lastname,
        "email" : current_user.email,
        "phone" : current_user.phone,
        "country" : current_user.country,
        "state" : current_user.state,
        "address" : current_user.address,
        "dob" : current_user.dob,
        "balance" : balance,
    }

    
    return render_template("user/dashboard.html", user=user)