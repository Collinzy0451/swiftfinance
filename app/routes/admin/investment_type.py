import os
from app import db, app
from flask import render_template, url_for, redirect, request, flash
from app.models.user import InvestmentType



# Utility function to save images
def save_image(image_data):
    import secrets
    from PIL import Image
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(image_data.filename)
    image_fn = random_hex + f_ext
    image_path = os.path.join(app.root_path, 'static/images/investment_type', image_fn)
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(image_path), exist_ok=True)

    # Resize the image if necessary
    output_size = (300, 300)
    i = Image.open(image_data)
    i.thumbnail(output_size)
    i.save(image_path)

    return image_fn


def delete_image(image_filename):
    if image_filename:  # Check if the image filename is not None or empty
        image_path = os.path.join(app.root_path, 'static/images/investment_type', image_filename)
        
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



@app.route("/investment-types", methods=['GET', 'POST'])
def addInvestmentTypes():
    investment_type = InvestmentType.query.all()

    if request.method == "POST":
        name = request.form.get('investmentTypeName')
        description = request.form.get('investmentTypeDescription')
        logo = request.files.get('img')  # Correct way to get uploaded file

        if logo:
            logo_filename = save_image(logo)
        else:
            logo_filename = None

        # Create and save the new InvestmentType
        gold_type = InvestmentType(name=name, description=description, logo=logo_filename)
        db.session.add(gold_type)
        db.session.commit()
        flash(f'{name} Investment Type Created successfully!', 'success')
        return redirect(url_for('addInvestmentTypes'))

    return render_template("admin/add_investment_type.html", investment_type=investment_type)


@app.route("/edit-investment-types/<int:investment_type_id>", methods=['GET', 'POST'])
def editInvestmentTypes(investment_type_id):
    investment_type = InvestmentType.query.get(investment_type_id)  # Get the actual object

    if not investment_type:
        flash("Investment type not found!", "danger")
        return redirect(url_for('addInvestmentTypes'))

    if request.method == "POST":
        name = request.form.get('investmentTypeName')
        description = request.form.get('investmentTypeDescription')
        logo = request.files.get('img')  # Correct way to get uploaded file

        # Delete existing image if new one is uploaded
        if logo and investment_type.logo:
            delete_image(investment_type.logo)

        # Save new logo
        logo_filename = save_image(logo) if logo else investment_type.logo

        # Update fields
        investment_type.name = name
        investment_type.description = description
        investment_type.logo = logo_filename

        db.session.commit()
        flash(f'{name} Investment Type Updated successfully!', 'success')
        return redirect(url_for('addInvestmentTypes'))

    return render_template("admin/edit_investment_type.html", investment_type=investment_type)





@app.route("/delete-investment-type/<int:investment_type_id>", methods=["POST"])
def deleteInvestmentType(investment_type_id):
    investment_type = InvestmentType.query.get_or_404(investment_type_id)

    # Delete the image file from the filesystem
    if investment_type.logo:
        delete_image(investment_type.logo)

    # Delete the investment type from the database
    db.session.delete(investment_type)
    db.session.commit()

    flash(f"{investment_type.name} has been deleted successfully.", "success")
    return redirect(url_for("addInvestmentTypes"))
