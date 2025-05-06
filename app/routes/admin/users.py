from app import app
from flask import render_template, redirect, url_for
from flask_login import  current_user, login_required
from app.models.user import User



@app.route('/users', methods=['GET', 'POST'])
@login_required
def users():
    if not current_user.is_admin:
        return(redirect(url_for('userDashboard')))
    
    users = User.query.all()

    return render_template('admin/users.html', users=users)












