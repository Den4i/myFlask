from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    name_ = StringField('логин', validators=[DataRequired()])
    pass_ = StringField('пароль', validators=[DataRequired()])



