from app import db
from app.models.user import User

# Fetch all users
users = User.query.all()

if users:
    for user in users:
        print(f"{user.id}: {user.firstname} {user.lastname} - {user.email}")
else:
    print("No users found.")
