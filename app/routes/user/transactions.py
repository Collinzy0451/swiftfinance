from app import app
from flask import render_template
from flask_login import current_user, login_required
from app.models.user import Transaction

@app.route('/transactions')
@login_required
def transactions():
    transactions = Transaction.query.filter_by(user_id=current_user.id).order_by(Transaction.id.desc()).all()
    return render_template("user/transactions.html", transactions=transactions)
