from sqlalchemy import func
from app import app, db
from flask import render_template, redirect, url_for
from flask_login import login_required, current_user
from app.models.user import InvestmentType, Investment

@app.route("/dashboard", methods=["GET", "POST"])
@login_required
def userDashboard(): 
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




    # Get all investment types (optional, depending on what you want to show)
    investment_types = InvestmentType.query.all()
    

    # Get investments for the current user
    investments = Investment.query.filter_by(user_id=current_user.id).all()
           
    total_investment_balance = db.session.query(func.sum(Investment.balance)).filter_by(user_id=current_user.id).scalar() or 0
    return render_template("user/user_dasboard.html", 
                           investment_types=investment_types, 
                           investments=investments, total_investment_balance=total_investment_balance, gold_investment=gold_investment, crypto_investment=crypto_investment, forex_investment=forex_investment, stock_investment=stock_investment)
