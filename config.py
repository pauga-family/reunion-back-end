import os
from datetime import timedelta
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'PLACEHOLDER KEY'
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'test-server'
    JWT_ACCESS_TOKEN_EXPIRES = os.environ.get('JWT expiration') or timedelta(days=30)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    