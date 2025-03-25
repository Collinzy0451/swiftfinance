from app import app
from flask import render_template


@app.route('/admin-settings', methods=['GET', 'POST'])
def adminSetting():
    
    return render_template('admin/settings.html')