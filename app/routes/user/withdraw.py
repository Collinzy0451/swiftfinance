from app import app
from flask import render_template
from flask_login import login_required, current_user
from app.models.user import User

@app.route('/withdraw')
@login_required
def withdraw():
    

    return render_template("user/withdraw.html")