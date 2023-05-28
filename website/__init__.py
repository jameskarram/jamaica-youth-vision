from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from functools import wraps

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'changethislater' #encrypting session data
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}" #location of database
    db.init_app(app)

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User
    print("about to create database")
    
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print("database created successfully")
    

    login_manager = LoginManager()
    login_manager.login_view = "views.home"
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    return app

