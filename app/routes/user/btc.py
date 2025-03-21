from app import app
from flask import render_template
from flask_login import login_required, current_user
from app.models.user import User

@app.route("/btc")
@login_required
def btc():


    return render_template("user/btc.html")