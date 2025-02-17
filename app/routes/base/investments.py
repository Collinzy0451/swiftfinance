from app import app
from flask import render_template

@app.route('/investments')
def investments():
    return render_template("base/investment.html")