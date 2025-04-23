from app.models.user import User
from app import app, db

# Fetch all users

with app.app_context():
    db.drop_all()
    db.create_all()
    users = User.query.all()
    print(users)

