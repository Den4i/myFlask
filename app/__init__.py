from flask import Flask
from flask_login import LoginManager, login_user
from flask_sqlalchemy import SQLAlchemy
import fdb

app = Flask(__name__)
app.config.from_object('config')

# SQLALCHEMY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'firebird+fdb://SYSDBA:zaUgD5Lt@195.98.79.37:3050/C:\SCAT\WORKBIN\DB\PROJECTS.FDB'
db = SQLAlchemy(app)

# Инициализируем его и задаем действие "входа"
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


from app import views, models
from .models import User

