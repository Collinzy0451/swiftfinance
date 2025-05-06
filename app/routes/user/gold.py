

from flask import request, redirect, url_for, flash, render_template
from flask_login import login_required, current_user
from decimal import Decimal
from app import db, app
from app.models.user import Investment, InvestmentType, Transaction



@app.route('/gold-investment', methods=['GET', 'POST'])
@login_required
def gold():
    user = current_user
    gold_investment = Investment.query.join(InvestmentType).filter(
        Investment.user_id == user.id,
        InvestmentType.name == 'Gold'
    ).first()

    return render_template("user/gold.html", gold_investment=gold_investment)




@app.route('/create-gold-investment', methods=['POST', 'GET'])
@login_required
def createGoldInvestment():
    amount = Decimal(request.form.get('amount'))
    duration = int(request.form.get('duration'))

    if amount > float(current_user.account_bal):
        flash("Insufficient account balance for this investment.", "danger")
        return redirect(url_for('gold'))  # or whatever route renders the HTML page

    if amount <= float(0):
        flash("Amount cannot be lesser than Zero", "danger")
        return redirect(url_for('gold'))

    # Get Gold Investment Type
    gold_type = InvestmentType.query.filter_by(name="Gold").first()
    if not gold_type:
        flash("Gold investment type is not configured in the system.", "danger")
        return redirect(url_for('gold'))

    # Check if user already has a gold investment
    investment = Investment.query.filter_by(user_id=current_user.id, type_id=gold_type.id).first()

    if investment:
        investment.invested_amount += amount
        investment.balance += amount
        investment.is_active = True
        transaction = Transaction(
            amount = amount,
            transaction_type = 'Account Debit For Gold Investment',
            user_id = current_user.id
        )
        db.session.add(transaction)
    else:
        investment = Investment(
            user_id=current_user.id,
            type_id=gold_type.id,
            invested_amount=amount,
            balance=amount,
            is_active=True
        )
        db.session.add(investment)
        transaction = Transaction(
            amount = amount,
            transaction_type = 'Account Debit For Gold Investment',
            user_id = current_user.id
        )
        db.session.add(transaction)

    # Deduct from user account balance
    current_user.account_bal -= amount

    db.session.commit()
    flash(f"Successfully invested ${amount} in Gold for {duration} week(s).", "success")
    return redirect(url_for('userDashboard'))  # Change to appropriate redirect

