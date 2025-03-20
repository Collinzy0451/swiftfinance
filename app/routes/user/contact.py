from app import app
from flask import render_template
from flask_login import login_required, current_user
from app.models.user import User

@app.route('/contact-us')
@login_required
def contactUs():
    

    return render_template("user/contact.html")