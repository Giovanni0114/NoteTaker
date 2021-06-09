from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_database(app):
    if not path.exists(f'website/{DB_NAME}'):
        db.create_all(app=app)
        print("Database has been created successfully")


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = 'test123'
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqllite:///{DB_NAME}"
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note  

    create_database(app)

    return app

