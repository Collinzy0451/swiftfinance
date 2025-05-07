from datetime import datetime
from app import app, db
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app.models.user import User
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
    output_size = (200, 200)
    i = Image.open(image_data)
    i.thumbnail(output_size)
    i.save(image_path)

    return image_fn


def delete_image(image_filename):
    if image_filename:  # Check if the image filename is not None or empty
        image_path = os.path.join(app.root_path, 'static/images/profile', image_filename)
        
        try:
            if os.path.exists(image_path):
                os.remove(image_path)
                return True
            else:
                return False  # File doesn't exist
        except Exception as e:
            print(f"Error deleting image file {image_filename}: {e}")
            return False  # Error occurred during deletion
    return False  # No image filename provided


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    user = {
        "fname" : current_user.firstname,
        "lname" : current_user.lastname,
        "email" : current_user.email,
        "phone" : current_user.phone,
        "country" : current_user.country,
        "state" : current_user.state,
        "address" : current_user.address,
        "dob" : current_user.dob,
        "profile_image": current_user.profile_image
    }
    return render_template("user/profile.html", user=user)

@app.route('/update-profile', methods=['GET', 'POST'])
@login_required
def updateProfile():
    user = User.query.get_or_404(current_user.id)

    if request.method == 'POST':
        firstname = request.form.get('fName')
        lastname = request.form.get('lName')
        email = request.form.get('email')
        phone = request.form.get('phone')
        country = request.form.get('country')
        state = request.form.get('state')
        address = request.form.get('address')
        dob_str = request.form.get('dob')
        profile_pics = request.files.get('profile')

        dob = None
        if dob_str and dob_str.strip():
            try:
                dob = datetime.strptime(dob_str.strip(), '%Y-%m-%d').date()
            except ValueError:
                flash("Invalid date format. Please use YYYY-MM-DD.", "danger")
                return redirect(url_for('updateProfile'))

        if profile_pics and profile_pics.filename != '':
            if user.profile_image and user.profile_image != 'default_profile.png':
                delete_image(user.profile_image)
            profile_filename = save_image(profile_pics)
            user.profile_image = profile_filename

        # Update user info
        user.firstname = firstname
        user.lastname = lastname
        user.email = email
        user.phone = phone
        user.country = country
        user.state = state
        user.address = address
        user.dob = dob

        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile'))