from app import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_bcrypt import Bcrypt
from app.models.user import User, db

bcrypt = Bcrypt(app)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        country = request.form.get('country')
        state = request.form.get('state')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')

        # Validate inputs
        if password != confirm_password:
            flash("Passwords do not match!", "error")
            return redirect(url_for('register'))

        # Check if email exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered!", "error")
            return redirect(url_for('register'))

        # Hash password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    
        # Create new user
        new_user = User(
            firstname=firstname,
            lastname=lastname,
            country=country,
            state=state,
            email=email,
            phone=phone,
            address=address,
            password_hash=hashed_password  # Use 'password' to store the hashed password
        )
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please log in.", "success")
        return redirect(url_for('login'))

    return render_template("register.html")
