from app import app
from flask import render_template
from flask_login import login_required, current_user
from app.models.user import User

@app.route('/forex')
@login_required
def forex():


    return render_template("user/forex.html")