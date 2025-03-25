from app import app
from flask import render_template
from app.models.user import User


# @app.route('/add-balance', methods=['GET', 'POST'])
# def addBalance(user_id):
#     user = User.query.get_or_404(user_id)
#     a = user.id
#     b= user.account_bal
#     c = user.firstname
#     print(f"the user {c} has an id of: {a}, and account bal: {b} ")
#     return render_template('admin/addBalance.html', user=user)


@app.route('/add-balance', methods=['GET', 'POST'])
def addBalance():
    
    return render_template('admin/addBalance.html')