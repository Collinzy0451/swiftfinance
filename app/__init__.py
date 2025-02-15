from flask import Flask
from config import Config
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Load config
app.config.from_object(Config)

# Ensure SECRET_KEY is set
if not app.config['SECRET_KEY']:  
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", Config.SECRET_KEY)

# Initialize database
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import routes after initializing db to avoid circular imports
from app.routes.base import *
from app.routes.user import *

# Create database tables (ensure this runs only once)
with app.app_context():
    db.create_all()
