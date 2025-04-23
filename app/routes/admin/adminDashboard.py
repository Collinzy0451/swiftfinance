from flask_login import current_user, login_required
from app import app
from flask import redirect, render_template, url_for
from app.models.user import User


@app.route('/admin', methods=['GET', 'POST'])
@login_required
def adminDashboard():
    if not current_user.is_admin:
        return(redirect(url_for('userDashboard')))
    users = User.query.all()
    count_User = User.query.count()

   
    return render_template('admin/adminDashboard.html', users=users, count_User=count_User)



