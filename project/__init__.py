from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os


app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
# App configurations using a config file (.py file in application root dr)
# app.config.from_object('config.DevelopmentConfig')
# set APP_SETTINGS= config.DevelopmentConfig in cmd
app.config.from_object(os.environ['APP_SETTINGS'])
# SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
# Create the SQLALchemy Object
db = SQLAlchemy(app)

from project.users.views import users_blueprint
from project.home.views import home_blueprint

# register blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)


from .models import User

login_manager.login_view = "users.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()
