from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
  # Create Flask app
  app= Flask(__name__)
  app.config['SECRET_KEY'] = 'asioqwhjdnsakdbuia'
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  db.init_app(app)

  # Manage user sessions
  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  @login_manager.user_loader
  def load_user(id):
    return User.query.get(int(id))

  # Import blueprints
  from .views import views
  from .auth import auth
  
  app.register_blueprint(views, url_prefix='/')
  app.register_blueprint(auth, url_prefix='/auth')

  # Create database
  from .models import User,Note
  create_database(app)

  return app

def create_database(app):
  if not path.exists('website/' + DB_NAME):
    with app.app_context():
      db.create_all()
      print('Created Database!')