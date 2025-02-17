from flask import Flask
from config import Config
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

# Load config
app.config.from_object(Config)


# Ensure SECRET_KEY is set
if not app.config['SECRET_KEY']:  
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", Config.SECRET_KEY)

# Initialize database
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


# Import routes after initializing db to avoid circular imports
from app.routes.base import *
from app.routes.user import *

# Create database tables (ensure this runs only once)
with app.app_context():
    db.create_all()
