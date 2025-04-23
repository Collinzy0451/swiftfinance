from decimal import Decimal
from app import app, db
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

from app.models.user import Investment, InvestmentType

@app.route('/crypto', methods=['GET','POST'])
@login_required
def crypto():

    user = current_user

    crypto_investment = Investment.query.join(InvestmentType).filter(
        Investment.user_id == user.id,
        InvestmentType.name == 'Crypto'
    ).first()

    investments = Investment.query.filter_by(user_id=current_user.id).all()

    return render_template("user/crypto.html", crypto_investment=crypto_investment, )




@app.route('/create-crypto-investment', methods=['POST', 'GET'])
@login_required
def createCryptoInvestment():
    amount = Decimal(request.form.get('amount'))
    duration = int(request.form.get('duration'))

    if amount > float(current_user.account_bal):
        flash("Insufficient account balance for this investment.", "danger")
        return redirect(url_for('crypto'))  # or whatever route renders the HTML page

    if amount <= float(0):
        flash("Amount cannot be lesser than Zero", "danger")
        return redirect(url_for('crypto'))
    
    # Get Gold Investment Type
    crypto_type = InvestmentType.query.filter_by(name="Crypto").first()
    if not crypto_type:
        flash("Crypto investment type is not configured in the system.", "danger")
        return redirect(url_for('crypto'))

    # Check if user already has a gold investment
    investment = Investment.query.filter_by(user_id=current_user.id, type_id=crypto_type.id).first()

    if investment:
        investment.invested_amount += amount
        investment.balance += amount
        investment.is_active = True
    else:
        investment = Investment(
            user_id=current_user.id,
            type_id=crypto_type.id,
            invested_amount=amount,
            balance=amount,
            is_active=True
        )
        db.session.add(investment)

    # Deduct from user account balance
    current_user.account_bal -= amount

    db.session.commit()
    flash(f"Successfully invested ${amount} in Crypto for {duration} week(s).", "success")
    return redirect(url_for('userDashboard'))  # Change to appropriate redirect
