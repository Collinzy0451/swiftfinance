from app import app, db
from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from app.models.user import Investment, InvestmentType, User

@app.route('/investment')
@login_required
def investment():
    investment_types = InvestmentType.query.all()
    investments = Investment.query.filter_by(user_id=current_user.id).all()

    user = current_user

    gold_investment = Investment.query.join(InvestmentType).filter(
        Investment.user_id == user.id,
        InvestmentType.name == 'Gold'
    ).first()

    crypto_investment = Investment.query.join(InvestmentType).filter(
        Investment.user_id == user.id,
        InvestmentType.name == 'Crypto'
    ).first()
    forex_investment = Investment.query.join(InvestmentType).filter(
        Investment.user_id == user.id,
        InvestmentType.name == 'Forex'
    ).first()
    stock_investment = Investment.query.join(InvestmentType).filter(
        Investment.user_id == user.id,
        InvestmentType.name == 'Stocks'
    ).first()
    
    return render_template("user/investments.html", investments=investments, stock_investment=stock_investment, forex_investment=forex_investment, crypto_investment=crypto_investment, gold_investment=gold_investment, investment_types=investment_types)




@app.route('/close-investment', methods=['POST'])
@login_required
def closeInvestment():
    try:
        investment_id = request.form.get("investment_id")
        investment = Investment.query.get(investment_id)

        if not investment or investment.user_id != current_user.id:
            flash("Investment not found or access denied.", "danger")
            return redirect(url_for('userDashboard'))

        if not investment.is_active:
            flash("This investment is already closed.", "info")
            return redirect(url_for('userDashboard'))
        
        user = current_user
        user.account_bal += investment.balance

        investment.balance = 0.00
        investment.invested_amount = 0.00
        investment.is_active = False
        investment.percentage_increase = 0.00
        investment.percentage_decrease = 0.00

        db.session.commit()
        flash(f"Successfully closed {investment.type.name} investment", "success")

    except Exception as e:
        db.session.rollback()
        flash(f"Error: {str(e)}", "danger")

    return redirect(url_for('userDashboard'))




