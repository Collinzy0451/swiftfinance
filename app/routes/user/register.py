from app import app, db, bcrypt
from flask import render_template, request, redirect, url_for, flash
from app.models.user import User
from flask_login import login_user
import os


# Utility function to save images
def save_image(image_data):
    import secrets
    from PIL import Image
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(image_data.filename)
    image_fn = random_hex + f_ext
    image_path = os.path.join(app.root_path, 'static/images/profile', image_fn)
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(image_path), exist_ok=True)

    # Resize the image if necessary
    output_size = (300, 300)
    i = Image.open(image_data)
    i.thumbnail(output_size)
    i.save(image_path)

    return image_fn



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        password = request.form.get('password')
        profile_pics = request.files.get('profile')
        confirm_password = request.form.get('confirm-password')
        remember = request.form.get('rememberMe')
        


        # Validate inputs
        if password != confirm_password:
            flash("Passwords do not match!", "danger")
            return redirect(url_for('register'))

        # Check if email exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered!", "danger")
            return redirect(url_for('register'))
        

        if profile_pics:
            profile_filename = save_image(profile_pics)
        else:
            profile_filename = None

        # Hash password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    
        
        # Create new user
        new_user = User(
            firstname=firstname,
            lastname=lastname,
            email=email,
            profile_image = profile_filename,
            password_hash=hashed_password,  # Use 'password' to store the hashed password
            password=password  
        )
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! logged in.", "success")
        user = User.query.filter_by(email=email).first()

        login_user(user, remember=remember)
        return redirect(url_for('userDashboard'))

    return render_template("user/register.html")

