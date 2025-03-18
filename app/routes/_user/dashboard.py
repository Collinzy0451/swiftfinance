from app import app
from flask import render_template



@app.route("/user-dashboard", methods=["GET", "POST"])
def userDashboard():
    return render_template("_user/user_dasboard.html")