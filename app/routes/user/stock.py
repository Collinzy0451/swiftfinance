from app import app, db
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app.models.user import User

@app.route('/stock', methods=['GET','POST'])
@login_required
def stock():

    if request.method == "POST":
        invested_amount = float(request.form.get('amount', 0))  # Ensure default value
        duration = request.form.get('duration')
        acc_bal = current_user.account_bal
        stock_bal = current_user.stock_bal

        if invested_amount > acc_bal or invested_amount <= 0:
            flash('Investment amount cannot be greater than account balance', 'danger')
            return(redirect(url_for('stock')))
        
        acc_bal -= invested_amount
        stock_bal += invested_amount

        current_user.account_bal = acc_bal
        current_user.stock_bal = stock_bal

        
        db.session.commit()
        flash("Stock Investment initiated Successfully", 'success')
        return(redirect(url_for('stock')))


    return render_template("user/stock.html")