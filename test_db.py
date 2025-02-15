from app.models.user import User
from app import app

# Fetch all users

with app.app_context():
    users = User.query.all()
    print(users)

    if users:
        for user in users:
            print(user)
            print(f"{user.id}: {user.firstname} {user.lastname} - {user.email}")
    else:
        print("No users found.")
