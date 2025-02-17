import os

class Config:
    SECRET_KEY = 'edff4242c61e83417c17b166052b8199e17bcca548a121220f86e4d61c134125'  
    SQLALCHEMY_DATABASE_URI = 'sqlite:///myDB.db'  # Change to PostgreSQL or MySQL if needed
    SQLALCHEMY_TRACK_MODIFICATIONS = False
