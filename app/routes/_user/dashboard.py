from app import app
from flask import render_template
from flask_login import login_required



@app.route("/user-dashboard", methods=["GET", "POST"])
@login_required
def userDashboard():
    return render_template("_user/user_dasboard.html")