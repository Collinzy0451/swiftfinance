from flask_login import current_user, login_required
from app import app
from flask import redirect, render_template, url_for


@app.route('/admin-settings', methods=['GET', 'POST'])
@login_required
def adminSetting():
    if not current_user.is_admin:
        return(redirect(url_for('userDashboard')))
    
    return render_template('admin/settings.html')