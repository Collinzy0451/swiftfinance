from app import app
from flask import render_template
from flask_login import login_required, current_user
from app.models.user import User

@app.route('/pay-with-crypto')
@login_required
def cryptoPayment():
    

    return render_template("user/cryptoPayment.html")