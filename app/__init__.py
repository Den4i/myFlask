import configparser
import os

from flask import Flask
from flask_login import LoginManager

from flask_sqlalchemy_session import flask_scoped_session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONF = configparser.RawConfigParser()
CONF.read(os.path.join(os.path.dirname(__file__), r'../config.cfg'))

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(32)

# SQLALCHEMY
db = CONF['DB']
uri = db['DB_DRIVER']+'://'+db['DB_USER']+':'+db['DB_PASS']+'@'+db['DB_IP_PORT']+'/'+db['DB_PATH']

engine = create_engine(uri)
session_factory = sessionmaker(bind=engine)
session = flask_scoped_session(session_factory, app)

# Инициализируем его и задаем действие "входа"
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return session.query(User).get(int(user_id))

from app.models import User
from app import views, models
