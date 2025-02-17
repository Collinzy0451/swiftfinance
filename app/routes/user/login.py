from app import app, bcrypt
from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required
from app.models.user import User

@app.route("/login", methods=["POST", "GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = request.form.get('rememberMe')

        user = User.query.filter_by(email=email).first()

        if user:
            if bcrypt.check_password_hash(user.password_hash, password):
                login_user(user, remember=remember)
                next_page = request.args.get('next')

                if next_page:
                    return redirect(next_page)
                else:
                    if user.is_admin:
                        flash('Admin Logged In Successfully', 'success')
                        return redirect(url_for('dashboard'))  # Change to your admin dashboard route
                    else:
                        flash('You have successfully Logged In', 'success')
                        return redirect(url_for('dashboard'))  # Change to your user dashboard route
            else:
                flash('Invalid Password', 'danger')
        else:
            flash('No account found with this email', 'danger')

    return render_template("user/login.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout Successful", 'success')
    return redirect(url_for('home'))
