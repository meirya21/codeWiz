from app import *
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, Length


class LoginValidation(FlaskForm):
    user_name = StringField('user_name', validators=[DataRequired(), Length(min=2, max=20)],
                                render_kw={'autofocus': True, 'placeholder': 'Enter User'})

    user_pass= PasswordField('user_pass', validators=[DataRequired(), Length(min=2, max=20)],
                                render_kw={'autofocus': True, 'placeholder': 'Enter Password'})