from app.models.user import User
from app import app, db

# Fetch all users

with app.app_context():
    users = User.query.all()
    print(users)

