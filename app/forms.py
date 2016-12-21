from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    name_ = StringField('name_', validators=[DataRequired()])
    pass_ = StringField('pass_', validators=[DataRequired()])



