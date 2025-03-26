from app import app, db
from flask import render_template, request, flash, url_for, redirect
from app.models.user import User


@app.route('/add-balance/<int:user_id>', methods=['GET', 'POST'])
def addBalance(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        acc_bal = request.form.get('account_bal')
        gold_bal = request.form.get('gold_bal')
        forex_bal = request.form.get('forex_bal')
        crypto_bal = request.form.get('crypto_bal')
        stock_bal = request.form.get('stock_bal')

        user.account_bal = acc_bal
        user.gold_bal = gold_bal
        user.forex_bal = forex_bal
        user.crypto_bal = crypto_bal
        user.stock_bal = stock_bal

        db.session.commit()
        flash(f'Balance of {user.firstname} {user.lastname} was updated successfully!', 'success')
        return redirect(url_for('adminDashboard'))

    return render_template('admin/addBalance.html', user=user)


# @app.route('/add-balance', methods=['GET', 'POST'])
# def addBalance():
    
#     return render_template('admin/addBalance.html')