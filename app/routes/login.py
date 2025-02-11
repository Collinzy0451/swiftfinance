from app import app, db
from flask import render_template, request, redirect, url_for, flash, session
from app.models.user import User
from werkzeug.security import check_password_hash

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):  # Use the check_password method
            session['user_id'] = user.id  # Store user session
            flash("Login successful!", "success")
            return redirect(url_for('home'))  # Redirect to your homepage or dashboard

        flash("Invalid email or password!", "error")

    return render_template("login.html")
