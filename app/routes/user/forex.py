from decimal import Decimal
from app import app, db
from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from app.models.user import Investment, InvestmentType, Transaction

@app.route('/forex', methods=['GET','POST'])
@login_required
def forex():

    user = current_user

    forex_investment = Investment.query.join(InvestmentType).filter(
        Investment.user_id == user.id,
        InvestmentType.name == 'Forex'
    ).first()


    return render_template("user/forex.html", forex_investment=forex_investment)




@app.route('/create-forex-investment', methods=['POST', 'GET'])
@login_required
def createForexInvestment():
    amount = Decimal(request.form.get('amount'))
    duration = int(request.form.get('duration'))

    if amount > float(current_user.account_bal):
        flash("Insufficient account balance for this investment.", "danger")
        return redirect(url_for('forex'))  # or whatever route renders the HTML page

    if amount <= float(0):
        flash("Amount cannot be lesser than Zero", "danger")
        return redirect(url_for('forex'))

    # Get Gold Investment Type
    investment_type = InvestmentType.query.filter_by(name="Forex").first()
    if not investment_type:
        flash("Forex investment type is not configured in the system.", "danger")
        return redirect(url_for('forex'))

    # Check if user already has a gold investment
    investment = Investment.query.filter_by(user_id=current_user.id, type_id=investment_type.id).first()

    if investment:
        investment.invested_amount += amount
        investment.balance += amount
        investment.is_active = True
        transaction = Transaction(
            amount = amount,
            transaction_type = 'Account Debit For Forex Investment',
            user_id = current_user.id
        )
        db.session.add(transaction)
    else:
        investment = Investment(
            user_id=current_user.id,
            type_id=investment_type.id,
            invested_amount=amount,
            balance=amount,
            is_active=True
        )
        db.session.add(investment)
        transaction = Transaction(
            amount = amount,
            transaction_type = 'Account Debit For Forex Investment',
            user_id = current_user.id
        )
        db.session.add(transaction)

    # Deduct from user account balance
    current_user.account_bal -= amount

    db.session.commit()
    flash(f"Successfully invested ${amount} in Forex for {duration} week(s).", "success")
    return redirect(url_for('userDashboard'))  # Change to appropriate redirect