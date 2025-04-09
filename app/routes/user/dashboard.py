from app import app
from flask import render_template
from flask_login import login_required, current_user


@app.route("/user-dashboard", methods=["GET", "POST"])
@login_required
def userDashboard():
    gold = current_user.gold_bal
    crypto = current_user.crypto_bal
    forex = current_user.forex_bal
    stock = current_user.stock_bal
    total_investment = gold + crypto + forex + stock
    return render_template("user/user_dasboard.html", total_investment=total_investment)