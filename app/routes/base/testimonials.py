from app import app
from flask import render_template

@app.route('/testimonials')
def testimonials():
    return render_template("base/testimonials.html")