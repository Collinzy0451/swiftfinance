from app import app
from flask import render_template


@app.route('/all-user', methods=['GET', 'POST'])
def users():
    
    return render_template('admin/users.html')












