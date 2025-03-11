from app import app
from flask import render_template
from flask_login import login_required, current_user
from app.models.user import User

@app.route('/settings')
@login_required
def settings():


    return render_template("user/settings.html")