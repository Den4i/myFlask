from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import configparser
import os

conf = configparser.RawConfigParser()
conf.read(os.path.join(os.path.dirname(__file__), r'../config.cfg'))

app = Flask(__name__)
app.config.from_object('config')


# SQLALCHEMY
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = conf['DB']['DB_DRIVER']+'://'+conf['DB']['DB_USER']+':'+conf['DB']['DB_PASS']+'@'+\
                                        conf['DB']['DB_IP_PORT']+'/'+conf['DB']['DB_PATH']
db = SQLAlchemy(app)

# Инициализируем его и задаем действие "входа"
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

from app.models import User
from app import views, models
