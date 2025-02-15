from app import app
from flask import render_template, request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        print("\nemail: " + email)
        print("password: " + password + "\n")

        pass

    return render_template("user/login.html")
