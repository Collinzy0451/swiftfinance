from app import app
from flask import render_template
from flask_login import login_required, current_user
from app.models.user import User

@app.route('/stock')
@login_required
def stock():


    return render_template("user/stock.html")