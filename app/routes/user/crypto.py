from app import app, db
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

@app.route('/crypto', methods=['GET','POST'])
@login_required
def crypto():
    if request.method == "POST":
        invested_amount = float(request.form.get('amount', 0))  # Ensure default value
        duration = request.form.get('duration')
        acc_bal = current_user.account_bal
        crypto_bal = current_user.crypto_bal

        if invested_amount > acc_bal:
            flash('Investment amount cannot be greater than account balance', 'danger')
            return(redirect(url_for('crypto')))
        
        acc_bal -= invested_amount
        crypto_bal += invested_amount

        current_user.account_bal = acc_bal
        current_user.crypto_bal = crypto_bal

        
        db.session.commit()
        flash("Crypto Investment initiated Successfully", 'success')
        return(redirect(url_for('crypto')))


    return render_template("user/crypto.html")