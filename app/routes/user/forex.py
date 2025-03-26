from app import app, db
from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from app.models.user import User

@app.route('/forex', methods=['GET','POST'])
@login_required
def forex():
    if request.method == "POST":
        invested_amount = float(request.form.get('amount', 0))  # Ensure default value
        duration = request.form.get('duration')
        acc_bal = current_user.account_bal
        forex_bal = current_user.forex_bal

        if invested_amount > acc_bal:
            flash('Investment amount cannot be greater than account balance', 'danger')
            return(redirect(url_for('forex')))
        
        acc_bal -= invested_amount
        forex_bal += invested_amount

        current_user.account_bal = acc_bal
        current_user.forex_bal = forex_bal

        
        db.session.commit()
        flash("Forex Investment initiated Successfully", 'success')
        return(redirect(url_for('forex')))


    return render_template("user/forex.html")