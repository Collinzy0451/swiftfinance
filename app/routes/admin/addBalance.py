from flask_login import current_user, login_required
from app import app, db
from flask import render_template, request, flash, url_for, redirect
from app.models.user import InvestmentType, User, Investment
from decimal import Decimal



@app.route('/add-balance/<int:user_id>', methods=['GET', 'POST'])
@login_required
def addBalance(user_id):
    if not current_user.is_admin:
        return(redirect(url_for('userDashboard')))
    
    user = User.query.get_or_404(user_id)

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

    
    return render_template('admin/addBalance.html', user=user, gold_investment=gold_investment, crypto_investment=crypto_investment, forex_investment=forex_investment, stock_investment=stock_investment)


@app.route('/account-balance/<int:user_id>', methods=['GET', 'POST'])
@login_required
def accountBalance(user_id):
    if not current_user.is_admin:
        return(redirect(url_for('userDashboard')))
    user = User.query.get_or_404(user_id)

    if request.method == 'POST':
        acc_bal = float(request.form.get('account_bal'))

        final_bal = user.account_bal + Decimal(str(acc_bal))
        user.account_bal = final_bal

        db.session.commit()
        flash(f'Account Balance of {user.firstname} {user.lastname} was updated successfully!', 'success')
        return redirect(url_for('addBalance',  user_id=user.id))
    

@app.route('/gold-balance/<int:user_id>', methods=['POST'])
@login_required
def goldBalance(user_id):
    if not current_user.is_admin:
        return redirect(url_for('userDashboard'))

    percent = request.form.get('amount')  # Your input name is 'gold_bal'
    action = request.form.get('action')

    try:
        percent = Decimal(percent)
        if action == 'loss':
            percent *= -1  # Negative if it's a loss

        # Fetch the gold investment only
        gold_type = InvestmentType.query.filter_by(name='Gold').first()
        if not gold_type:
            flash("Gold investment type not found.", "warning")
            return redirect(url_for('addBalance', user_id=user_id))

        investment = Investment.query.filter_by(user_id=user_id, type_id=gold_type.id).first()
        if not investment:
            flash("Gold investment not found for this user.", "warning")
            return redirect(url_for('addBalance', user_id=user_id))

        change = investment.balance * (percent / 100)
        
        if investment.balance + change < 0:
            flash('Investment cannot be lesser than zero', 'danger')
            return redirect(url_for('addBalance', user_id=user_id))
        
        investment.balance += change

        investment.percentage_increase = percent if percent > 0 else 0
        investment.percentage_decrease = abs(percent) if percent < 0 else 0

        db.session.commit()
        flash(f"Gold balance updated with a {'Profit' if percent > 0 else 'Loss'} of {abs(percent)}%.", "success")

    except Exception as e:
        db.session.rollback()
        flash(f"Error updating gold balance: {str(e)}", "danger")

    return redirect(url_for('addBalance', user_id=user_id))


@app.route('/crypto-balance/<int:user_id>', methods=['POST'])
@login_required
def cryptoBalance(user_id):
    if not current_user.is_admin:
        return redirect(url_for('userDashboard'))

    percent = request.form.get('amount')  # Your input name is 'gold_bal'
    action = request.form.get('action')

    try:
        percent = Decimal(percent)
        if action == 'loss':
            percent *= -1  # Negative if it's a loss

        # Fetch the gold investment only
        crypto_type = InvestmentType.query.filter_by(name='Crypto').first()
        if not crypto_type:
            flash("Crypto investment type not found.", "warning")
            return redirect(url_for('addBalance', user_id=user_id))

        investment = Investment.query.filter_by(user_id=user_id, type_id=crypto_type.id).first()
        if not investment:
            flash("Crypto investment not found for this user.", "warning")
            return redirect(url_for('addBalance', user_id=user_id))

        change = investment.balance * (percent / 100)
        
        if investment.balance + change < 0:
            flash('Investment cannot be lesser than zero', 'danger')
            return redirect(url_for('addBalance', user_id=user_id))
        
        investment.balance += change

        investment.percentage_increase = percent if percent > 0 else 0
        investment.percentage_decrease = abs(percent) if percent < 0 else 0

        db.session.commit()
        flash(f"Crypto balance updated with a {'Profit' if percent > 0 else 'Loss'} of {abs(percent)}%.", "success")

    except Exception as e:
        db.session.rollback()
        flash(f"Error updating forex balance: {str(e)}", "danger")

    return redirect(url_for('addBalance', user_id=user_id))


@app.route('/forex-balance/<int:user_id>', methods=['POST'])
@login_required
def forexBalance(user_id):
    if not current_user.is_admin:
        return redirect(url_for('userDashboard'))

    percent = request.form.get('amount')  # Your input name is 'gold_bal'
    action = request.form.get('action')

    try:
        percent = Decimal(percent)
        if action == 'loss':
            percent *= -1  # Negative if it's a loss

        # Fetch the gold investment only
        forex_type = InvestmentType.query.filter_by(name='Forex').first()
        if not forex_type:
            flash("Forex investment type not found.", "warning")
            return redirect(url_for('addBalance', user_id=user_id))

        investment = Investment.query.filter_by(user_id=user_id, type_id=forex_type.id).first()
        if not investment:
            flash("Forex investment not found for this user.", "warning")
            return redirect(url_for('addBalance', user_id=user_id))

        change = investment.balance * (percent / 100)
        
        if investment.balance + change < 0:
            flash('Investment cannot be lesser than zero', 'danger')
            return redirect(url_for('addBalance', user_id=user_id))
        
        investment.balance += change

        investment.percentage_increase = percent if percent > 0 else 0
        investment.percentage_decrease = abs(percent) if percent < 0 else 0

        db.session.commit()
        flash(f"Forex balance updated with a {'Profit' if percent > 0 else 'Loss'} of {abs(percent)}%.", "success")

    except Exception as e:
        db.session.rollback()
        flash(f"Error updating forex balance: {str(e)}", "danger")

    return redirect(url_for('addBalance', user_id=user_id))


@app.route('/stocks-balance/<int:user_id>', methods=['POST'])
@login_required
def stockBalance(user_id):
    if not current_user.is_admin:
        return redirect(url_for('userDashboard'))

    percent = request.form.get('amount')  # Your input name is 'gold_bal'
    action = request.form.get('action')

    try:
        percent = Decimal(percent)
        if action == 'loss':
            percent *= -1  # Negative if it's a loss

        # Fetch the gold investment only
        stock_type = InvestmentType.query.filter_by(name='Stocks').first()
        if not stock_type:
            flash("Stocks investment type not found.", "warning")
            return redirect(url_for('addBalance', user_id=user_id))

        investment = Investment.query.filter_by(user_id=user_id, type_id=stock_type.id).first()
        if not investment:
            flash("Stocks investment not found for this user.", "warning")
            return redirect(url_for('addBalance', user_id=user_id))

        change = investment.balance * (percent / 100)
        
        if investment.balance + change < 0:
            flash('Investment cannot be lesser than zero', 'danger')
            return redirect(url_for('addBalance', user_id=user_id))
        
        investment.balance += change

        investment.percentage_increase = percent if percent > 0 else 0
        investment.percentage_decrease = abs(percent) if percent < 0 else 0

        db.session.commit()
        flash(f"Stocks balance updated with a {'Profit' if percent > 0 else 'Loss'} of {abs(percent)}%.", "success")

    except Exception as e:
        db.session.rollback()
        flash(f"Error updating stocks balance: {str(e)}", "danger")

    return redirect(url_for('addBalance', user_id=user_id))



