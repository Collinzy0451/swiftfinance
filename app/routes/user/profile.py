from app import app
from flask import render_template
from flask_login import login_required, current_user


@app.route('/profile')
def profile():
    user = {
        "fname" : current_user.firstname,
        "lname" : current_user.lastname,
        "email" : current_user.email,
        "phone" : current_user.phone,
        "country" : current_user.country,
        "state" : current_user.state,
        "address" : current_user.address,
        "dob" : current_user.dob,
    }
    return render_template("user/profile.html", user=user)