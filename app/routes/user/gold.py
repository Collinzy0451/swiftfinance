from app import app, db
from flask import render_template, request, flash, redirect,url_for
from flask_login import login_required, current_user

@app.route('/gold', methods=['GET','POST'])
@login_required
def gold():
    if request.method == "POST":
        invested_amount = float(request.form.get('amount', 0))  # Ensure default value
        duration = request.form.get('duration')
        acc_bal = current_user.account_bal
        gold_bal = current_user.gold_bal

        if invested_amount > acc_bal:
            flash('Investment amount cannot be greater than account balance', 'danger')
            return(redirect(url_for('gold')))
        
        acc_bal -= invested_amount
        gold_bal += invested_amount

        current_user.account_bal = acc_bal
        current_user.gold_bal = gold_bal

        
        db.session.commit()
        flash("Gold Investment initiated Successfully", 'success')
        return(redirect(url_for('gold')))
       
    return render_template("user/gold.html")