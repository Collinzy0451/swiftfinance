from decimal import Decimal
from app import app, db
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from app.models.user import Investment, InvestmentType, User

@app.route('/stock', methods=['GET','POST'])
@login_required
def stock():
    user = current_user

    stock_investment = Investment.query.join(InvestmentType).filter(
        Investment.user_id == user.id,
        InvestmentType.name == 'Stocks'
    ).first()

    return render_template("user/stock.html", stock_investment=stock_investment)



@app.route('/create-stock-investment', methods=['POST', 'GET'])
@login_required
def createStockInvestment():
    amount = Decimal(request.form.get('amount'))
    duration = int(request.form.get('duration'))

    if amount > float(current_user.account_bal):
        flash("Insufficient account balance for this investment.", "danger")
        return redirect(url_for('stock'))  # or whatever route renders the HTML page
    
    if amount <= float(0):
        flash("Amount cannot be lesser than Zero", "danger")
        return redirect(url_for('stock'))  # or whatever route renders the HTML page

    # Get Gold Investment Type
    investment_type = InvestmentType.query.filter_by(name="Stocks").first()
    if not investment_type:
        flash("Stock investment type is not configured in the system.", "danger")
        return redirect(url_for('stock'))

    # Check if user already has a gold investment
    investment = Investment.query.filter_by(user_id=current_user.id, type_id=investment_type.id).first()

    if investment:
        investment.invested_amount += amount
        investment.balance += amount
        investment.is_active = True
    else:
        investment = Investment(
            user_id=current_user.id,
            type_id=investment_type.id,
            invested_amount=amount,
            balance=amount,
            is_active=True
        )
        db.session.add(investment)

    # Deduct from user account balance
    current_user.account_bal -= amount

    db.session.commit()
    flash(f"Successfully invested ${amount} in Stocks for {duration} week(s).", "success")
    return redirect(url_for('userDashboard'))  # Change to appropriate redirect