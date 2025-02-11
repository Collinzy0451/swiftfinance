from app import app
from flask import render_template

@app.route('/transactions')
def transactions():
    return render_template("transactions.html")