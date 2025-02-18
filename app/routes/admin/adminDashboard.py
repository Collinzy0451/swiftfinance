from app import app
from flask import render_template
from app.models.user import User


@app.route('/admin', methods=['GET', 'POST'])
def adminDashboard():
    users = User.query.all()
    count_User = User.query.count()
    print(users)
    return render_template('admin/adminDashboard.html', users=users, count_User=count_User)
