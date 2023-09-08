from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

def create_app(config_name):
    app = Flask(__name__)
    user = 'root'
    password = 'sena'
    url = 'localhost'
    db = 'test'
    full_url = f'mysql://{user}:{password}@{url}/{db}'
    app.config['SQLALCHEMY_DATABASE_URI'] = full_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app
