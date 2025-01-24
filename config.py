import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT')
    # SECURITY_LOGIN_URL = '/auth/login'
    # SECURITY_LOGIN_USER_TEMPLATE = 'login.html'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
